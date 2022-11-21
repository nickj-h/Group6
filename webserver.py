

from flask import Flask, Blueprint, render_template


hello = Blueprint('hello', __name__)


@hello.route('/')
def show_map():
    return render_template('testmap4.html')
   # return 'Hello, World!'

#uses PlotlyJS to have user-interactive map
@hello.route('js')
def show_jsmap():
    return render_template('map_plotlyJS.html')
    
#renders the florida state interface data. This gets called when a state is clicked
@hello.route('florida')
def show_fl():
    return render_template('florida.html')
    
    
'''
@hello.route('/')
def hello_world():
    return 'Hello, World!'
'''
if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(hello, url_prefix='/')

    app.run()

