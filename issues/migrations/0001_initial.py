# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Issue'
        db.create_table('issues_issue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='issues', to=orm['issues.Category'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(related_name='issues', to=orm['articleflow.Article'])),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='issues_submitted', null=True, blank=True, to=orm['auth.User'])),
            ('error', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('current_status', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='current_status_of', null=True, blank=True, to=orm['issues.IssueStatus'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 4, 0, 0))),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('issues', ['Issue'])

        # Adding model 'IssueStatus'
        db.create_table('issues_issuestatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statuses', to=orm['issues.Issue'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 4, 0, 0))),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('issues', ['IssueStatus'])

        # Adding model 'Category'
        db.create_table('issues_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 4, 0, 0))),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('issues', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Issue'
        db.delete_table('issues_issue')

        # Deleting model 'IssueStatus'
        db.delete_table('issues_issuestatus')

        # Deleting model 'Category'
        db.delete_table('issues_category')


    models = {
        'articleflow.article': {
            'Meta': {'object_name': 'Article'},
            'article_extras': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'article_dont_use'", 'null': 'True', 'blank': 'True', 'to': "orm['articleflow.ArticleExtras']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 4, 0, 0)'}),
            'current_articlestate': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'current_article'", 'null': 'True', 'blank': 'True', 'to': "orm['articleflow.ArticleState']"}),
            'current_state': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'current_articles'", 'null': 'True', 'blank': 'True', 'to': "orm['articleflow.State']"}),
            'doi': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['articleflow.Journal']"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'pubdate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'si_guid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'articleflow.articleextras': {
            'Meta': {'object_name': 'ArticleExtras'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'article_extras_dont_use'", 'to': "orm['articleflow.Article']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 4, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_errors_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_issues_legacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_issues_pdf': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_issues_si': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_issues_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_issues_xml': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_issues_xmlpdf': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_warnings': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'articleflow.articlestate': {
            'Meta': {'object_name': 'ArticleState'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'article_states'", 'to': "orm['articleflow.Article']"}),
            'assignee': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 4, 0, 0)'}),
            'from_transition': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'articlestates_created'", 'null': 'True', 'blank': 'True', 'to': "orm['articleflow.Transition']"}),
            'from_transition_user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'articlestates_created'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['articleflow.State']"})
        },
        'articleflow.journal': {
            'Meta': {'object_name': 'Journal'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'articleflow.state': {
            'Meta': {'ordering': "['progress_index']", 'object_name': 'State'},
            'auto_assign': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'progress_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'worker_groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'state_assignments'", 'default': 'None', 'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        'articleflow.transition': {
            'Meta': {'object_name': 'Transition'},
            'allowed_groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'allowed_transitions'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'disallow_open_items': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'from_state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'possible_transitions'", 'to': "orm['articleflow.State']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'preference_weight': ('django.db.models.fields.IntegerField', [], {}),
            'to_state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'possible_last_transitions'", 'to': "orm['articleflow.State']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'issues.category': {
            'Meta': {'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 4, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'issues.issue': {
            'Meta': {'ordering': "['created']", 'object_name': 'Issue'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issues'", 'to': "orm['articleflow.Article']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issues'", 'to': "orm['issues.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 4, 0, 0)'}),
            'current_status': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'current_status_of'", 'null': 'True', 'blank': 'True', 'to': "orm['issues.IssueStatus']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'error': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'issues_submitted'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"})
        },
        'issues.issuestatus': {
            'Meta': {'object_name': 'IssueStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 4, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'to': "orm['issues.Issue']"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['issues']