import json
import sys
import os 
import flask 
import requests
application = flask.Flask(__name__)

@application.route('/')
def hello_world():
    google_url = "https://www.google.com"
    requests.get(google_url)
       

    return flask.jsonify({
        'name': str(requests.get(google_url)),
        'python_version': sys.version.split(" ", 2)[0],
        'environment': os.environ.copy(),
        'flask_version': flask.__version__,
    })

if __name__ == '__main__':
    port = int(os.environ.get("FLASK_RUN_PORT", 8000))
    application.run(host='0.0.0.0', debug=True, port=port)
