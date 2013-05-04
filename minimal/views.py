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
    req = Request(environ)
    method = req.method
    
    if method in ('POST', 'PUT'):
        content = req.POST['data']
        
        hashFunction = hashlib.md5()
        hashFunction.update(content)
        fileName = hashFunction.hexdigest()
        
        if not os.path.exists(STORAGE_DIRECTORY):
            os.makedirs(STORAGE_DIRECTORY)
            
        #TODO: Allow ability to edit annotations in the future? In which case cleanup old hash?
        fileObj = open(STORAGE_DIRECTORY + "/" + fileName, 'w')
        fileObj.writelines(content)
        fileObj.close();
        
        resp = Response(json.dumps({
            'fileName' : fileName
        }))
        resp.headers.add('Access-Control-Allow-Origin', '*')

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
        