from bottle import route, run, template
import sys

@route('/')
def index():
    return "Hello World"

run(host="0.0.0.0", port=sys.argv[1], reloader=True)