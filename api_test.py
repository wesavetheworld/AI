import requests
import simplejson


print "should give invalid data"
data = {
    'test': 'this is a test'
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text


print "should give unable to parse"
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data='hahaha}')
print r.text


print "echo"
data = {
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text

print "update pubdate: invalid date format"
data = {
    'pubdate': '2013-12-31 00:00:00'
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text

print "update pubdate: success"
data = {
    'pubdate': '2013-12-31'
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text

print "update state: nonexistant state"
data = {
    'state': 'lala',
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text

print "update state: nonexistant state"
data = {
    'state': 'lala',
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text

print "update state: success"
data = {
    'state': 'Ingested',
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text

print "Shouldn't do anything"
data = {
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text

print "Should complain about a fake user"
data = {
    'state': 'Delivered',
    'state_change_user': 'fake_user',
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text

print "Should reset article to new effected by jlabarba"
data = {
    'state': 'New',
    'state_change_user': 'jlabarba',
}
r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999', data=simplejson.dumps(data))
print r.text


##### PUT errorset tests #####
print "Errorset PUT"
data = {
    'source': 'ariesPull',
    'errors': 'error: stuff'
}

r = requests.put('http://10.135.2.181:8000/api/article/pone.9999999/errorset/', data=simplejson.dumps(data))
print r.text


