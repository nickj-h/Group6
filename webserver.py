

from flask import Flask, Blueprint, render_template


hello = Blueprint('hello', __name__)


@hello.route('/')
def show_map():
    return render_template('testmap.html')
   # return 'Hello, World!'

'''
@hello.route('/')
def hello_world():
    return 'Hello, World!'
'''
if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(hello, url_prefix='/')

    app.run()
