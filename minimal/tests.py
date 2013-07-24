from webtest import TestApp
from views import *
from webob import exc

import json
import hashlib

HOST_ADDRESS = 'http://127.0.0.1:6543'

def testHashingFunctionality():
    app = TestApp(hasher)
    annotation = "This is a sample piece of annotation"

    postData = {
        'data' : annotation
    }
    resp = app.post(HOST_ADDRESS + "/annotate/", postData)

    assert resp.status == '200 OK'

    body = json.loads(resp.body)
    hashFunction = hashlib.md5()
    hashFunction.update(annotation)
    hashedData = hashFunction.hexdigest()
    
    # Make sure the body is a json in the format {"fileName" : <actualFileName>}
    assert 'fileName' in body
    # Make sure the file name is a md5 hash of the annotation
    assert body['fileName'] == hashedData
    
    resp = app.get(HOST_ADDRESS + "/annotate?file=" + hashedData)
    
    # Now do a get request with the the hash as the file name parameter and make
    # sure that the annotation is returned
    assert resp.status == '200 OK'
    assert resp.body == annotation
    
testHashingFunctionality()    