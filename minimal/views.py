'''
To run the app using paster, use the command
paster serve minimal/minimal.ini --reload
'''

from webob import Request, Response, exc

import os
import hashlib
import json

STORAGE_DIRECTORY = '/tmp/annotate'

def hasher(environ, start_response):
    import pdb; pdb.set_trace()
    req = Request(environ)
    content = req.body
    method = req.method
    
    if method in ('POST', 'PUT'):
        hashFunction = hashlib.md5()
        hashFunction.update(content)
        fileName = hashFunction.hexdigest()
        
        fileObj = open(STORAGE_DIRECTORY + "/" + fileName, 'w')
        fileObj.writelines(content)
        
        resp = Response(json.dumps({
            'fileName' : fileName
        }))
        return resp(environ, start_response)
    
    elif method == 'GET':
        fileName = req.params.get('file')
        if not fileName:
            raise exc.HTTPBadRequest('Filename required')
        try:
            storageFile = open(STORAGE_DIRECTORY + "/" + fileName, 'r')
        except IOError:
            raise exc.HTTPBadRequest('Invalid filename: %s' % fileName)
        
        resp = Response()
        resp.body = storageFile.read()
        return resp(environ, start_response)
        