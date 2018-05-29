from flask import request

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! " + request.args.get('name', "Jason")


@app.route('/bottles')
def bottles():
    _ = ''
    for count in range(100, 0, -1):
        _ += str(count) + ' bottles of beer on the wall<br/>'
    return "<html><h5>Hello, World! " + \
           request.args.get('name', "Jason") + "</h5>" + _ + "</html>"
