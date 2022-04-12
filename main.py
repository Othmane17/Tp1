from bottle import route, run
import sys
from helpers import hello

@route('/')
def index():
    return "Hello World"


run(host="0.0.0.0", port=sys.argv[1], reloader=True)
