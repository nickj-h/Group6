from flask import Flask, Blueprint, render_template
hello = Blueprint('hello', __name__)

@hello.route('/')
def home():
    return render_template('homepage.html')
   # return 'Hello, World!'

@hello.route('management')
def show_management():
    return render_template('management.html')

@hello.route('business')
def show_business():
    return render_template('business.html')

@hello.route('computer')
def show_computer():
    return render_template('computer.html')

@hello.route('architecture')
def show_architecture():
    return render_template('Architecture.html')

@hello.route('life')
def show_life():
    return render_template('life.html')

#uses PlotlyJS to have user-interactive map. use /js route in URL
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

