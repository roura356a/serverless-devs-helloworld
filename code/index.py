import logging
HELLO_WORLD = b'Hola Mundo!\n'


def handler(environ, start_response):
    context = environ['fc.context']
    request_uri = environ['fc.request_uri']
    for k, v in environ.items():
      if k.startswith('HTTP_'):
        pass
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [HELLO_WORLD]