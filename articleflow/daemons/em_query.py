import pyodbc
import re
import pytz

from ai import settings

from articleflow.models import Journal
import datetime

import logging
logger = logging.getLogger(__name__)

PAC_TZ = pytz.timezone('US/Pacific')
EAST_TZ = pytz.timezone('US/Eastern')

def get_journal_from_doi(doi):
    match = re.match('.*(?=\.)', doi)
    
    if not match:
        raise ValueError('Could not find a journal short_name in doi, %s' % doi)
    short_name = re.match('.*(?=\.)', doi).group(0)
    
    try:
        return Journal.objects.get(short_name=short_name)
    except Journal.DoesNotExist:
        raise ValueError("doi prefix, %s, does not match any known journal" % short_name)

class MSSQLConnection(object):
    def __init__(self, host, user, password, port=1433, database=''):
        cnx_settings = 'DRIVER={freeTDS};SERVER=%s;PORT=%d;DATABASE=%s;UID=%s;PWD=%s;TDS_VERSION=8.0' % (host, port, database, user, password)
        self.cnxn = pyodbc.connect(cnx_settings)
        self.cursor = self.cnxn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.cnxn.close()
        
class EMConnection(MSSQLConnection):
    def __init__(self):
        super(EMConnection, self).__init__(\
            host=settings.EM_REPORTING_DATABASE['HOST'],
            port=settings.EM_REPORTING_DATABASE['PORT'],
            user=settings.EM_REPORTING_DATABASE['USER'],
            password=settings.EM_REPORTING_DATABASE['PASSWORD'])
        self.cursor.execute('USE %s' % 'PONE')
        
class EMQueryConnection(EMConnection):
    def get_pubdate(self, doi):
        # will throw ValueError if can't figure out journal from DOI
        # will throw LookupError if EM doesn't return good data
        journal = get_journal_from_doi(doi)
        #self.cursor.execute('USE %s' % journal.em_name)
        self.cursor.execute(
            """
            SELECT actual_online_pub_date
            FROM document d
            WHERE d.doi like '%%%s'
            """ % doi)
        
        r = self.cursor.fetchall()

        if len(r) == 0:
            raise LookupError("DOI: %s not found in EM" % doi)
        if len(r) > 1:
            raise LookupError("Multiple entries found for DOI: %s" % doi)
        
        return r[0][0]

    def get_all_pubdates(self):
        journals = Journal.objects.all()
        r = []
        for journal in journals:
            self.cursor.execute('USE %s' % journal.em_db_name)
            self.cursor.execute(
                """
                SELECT
                  doi,
                  actual_online_pub_date as 'pubdate',
                  documentid,
                  pubdnumber,
                  revision as rev_max,
                  category
                FROM document d
                WHERE d.doi is not null
                  AND d.revision =
                  (SELECT MAX(d_sub.revision) as rev_max FROM document d_sub WHERE d_sub.documentid = d.documentid) 
                """)
            r += self.cursor.fetchall()
        return r
    
    def sync_all_after_mtime(self, mtime=None):
        if not mtime:
            mtime = datetime.datetime.now(tz=PAC_TZ) - datetime.timedelta(hours=1)
        journals = Journal.objects.all()
        r = []
        for journal in journals:
            self.cursor.execute('USE %s' % journal.em_db_name)
            try:
                self.cursor.execute(
                """
                SELECT
                  doi,
                  actual_online_pub_date as 'pubdate',
                  documentid,
                  pubdnumber,
                  revision as rev_max,
                  Row_LastModified_Timestamp as last_modified
                FROM document d
                WHERE d.doi is not null
                  AND d.revision =
                  (SELECT MAX(d_sub.revision) as rev_max FROM document d_sub WHERE d_sub.documentid = d.documentid) 
                  AND d.Row_LastModified_Timestamp >= '%s'
                """ % mtime.astimezone(EAST_TZ).strftime('%Y-%m-%d %H:%M:%S'))
                r += self.cursor.fetchall()
            except Exception, e:
                logger.error("Error fetching pubdates from %s: %s" % (journal, str(e)))
                
        return r

def main():
    with EMQueryConnection() as emq:
        print emq.get_pubdate('pone.0053871')
        d = datetime.datetime.now(tz=PAC_TZ)
        print emq.sync_all_after_mtime()

if __name__ == '__main__':
    main()
