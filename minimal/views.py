'''
To run the app using paster, use the command
paster serve minimal/minimal.ini --reload
'''

from webob import Request, Response, exc

import os
import hashlib

STORAGE_FILE_PATH = '/tmp/storageFile.txt'

def hasher(environ, start_response):
    import pdb; pdb.set_trace()
    req = Request(environ)
    content = req.body
    method = req.method
    
    if method in ('POST', 'PUT'):
        hashedContent = hashString('md5', content)
        storageFile = open(STORAGE_FILE_PATH, 'w')
        storageFile.writelines(hashedContent)
        
        resp = Response('Your contents have been hashed!')
        return resp(environ, start_response)
    
    elif method == 'GET':
        storageFile = open(STORAGE_FILE_PATH, 'r')
        resp = Response()
        resp.body = storageFile.read()
        return resp(environ, start_response)

def hashString(hashAlgorithm, content):
    try:
        hashFunction = getattr(hashlib, hashAlgorithm)()
    except AttributeError:
        hashFunction = getattr(hashlib, 'md5')()
    
    hashFunction.update(content)
    return hashFunction.digest()
        