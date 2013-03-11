from webob import Request, Response, exc

import os
import hashlib

STORAGE_FILE_PATH = '/tmp/storageFile.txt'

class SimpleApp:
    def __init__(self, storage_file_path=STORAGE_FILE_PATH):
        self.storage_file_path = storage_file_path
    
    def __call__(self, environ, start_response):
        req = Request(environ)
        content = req.body
        method = req.method
        path = self.cleanPath(req.path)

        if path != 'annotate':
            raise exc.HTTPBadRequest('Invalid page: %s' % req.url)
        
        if method == 'POST' or method == 'PUT':
            hashedContent = self.hashString('md5', content)
            storageFile = open(self.storage_file_path, 'w')
            storageFile.writelines(str(hashedContent))
            
            resp = Response('Your contents have been hashed!')
            return resp(environ, start_response)
        
        elif method == 'GET':
            storageFile = open(self.storage_file_path, 'r')
            resp = Response()
            resp.body = storageFile.read()
            return resp(environ, start_response)
    
    def cleanPath(self, path):
        """
        >>> a = SimpleApp()
        >>> a.cleanPath('/annotate')
        'annotate'
        >>> a.cleanPath('/annotate/')
        'annotate'
        """
        result = path.lstrip('/')
        result = os.path.normpath(result)
        return result
    
    def hashString(self, hashAlgorithm, content):
        try:
            hashFunction = getattr(hashlib, hashAlgorithm)()
        except AttributeError:
            hashFunction = getattr(hashlib, 'md5')()
        
        hashFunction.update(content)
        return hashFunction.digest()
        
def main(global_config, **setings):
    return SimpleApp()