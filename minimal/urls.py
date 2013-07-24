from werkzeug.routing import Map, Rule, NotFound, RequestRedirect
from httplib import HTTPException

import views

url_map = Map([
    Rule('/annotate', endpoint='hasher'),
    #Format for get request '/annotate?file=hashedFileName'
    Rule('/annotate<queryParam>', endpoint='hasher')
])

def url_mapper(environ, start_response):
    urls = url_map.bind_to_environ(environ)
    try:
        endpoint, args = urls.match()
    except HTTPException, e:
        return e(environ, start_response)
    
    names = endpoint.split('.')
    view = views
    for name in names:
        if not hasattr(view, name):
            __import__(view.__name__, None, None, [name])
        try:
            view = getattr(view, name)
        except e, AttributeError:
            return HTTPException(environ, start_response)
    try:
        response = view(environ, start_response)
    except Exception, exc:
        response = exc
    return response
        
def main(global_config, **setings):
    return url_mapper