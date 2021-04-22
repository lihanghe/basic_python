import json
import sys

from wsgiref.util import setup_testing_defaults

def application(environ, start_response):
    setup_testing_defaults(environ)

    pythonVersion = 'Python ' + sys.version.split(" ", 2)[0]
    start_response(status, headers)

    response = {
        'pythonVersion': pythonVersion,
        'environment': os.environ.copy(),
    }

    return [json.dumps(response).encode('utf-8')]
