#!flask/bin/python

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "PING ... ping ... PING"

if __name__ == '__main__':
    app.run(debug=True)
