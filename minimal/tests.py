from webtest import TestApp
from apps import *
from webob import exc

import hashlib

HOST_ADDRESS = 'http://127.0.0.1:6543'

def testSimpleApp():
    app = TestApp(SimpleApp())
    postData = {
        'key1' : 'value1',
        'key2' : 'value2',
        'key3' : 'value3'
    }
    resp = app.post(HOST_ADDRESS + '/annotate/', postData)
    
    assert resp.status == '200 OK'
    
    hashFunction = hashlib.md5()
    hashFunction.update("key3=value3&key2=value2&key1=value1")
    
    hashedData = hashFunction.digest()
    
    resp = app.get(HOST_ADDRESS + '/annotate')
    assert resp.body == hashedData

    #Check that having a trailing / doesn't break the app
    resp = app.get(HOST_ADDRESS + '/annotate/')
    assert resp.body == hashedData
    
    #Send in an invalid url and make sure we get the right exception
    try:
        resp = app.get(HOST_ADDRESS)
    except Exception, e:
        assert type(e) == exc.HTTPBadRequest