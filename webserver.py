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


#/stateMap/main is the default ma.
# upon clicking a state, javascript calls the /stateMap/id route where id is the 2-letter state code  e.g. stateMap/FL
# and flask serves the appropriate data

@hello.route('stateMap/<id>')
def show_stateMap(id):
    if id == "main":
        return render_template('stateMap.html') 
    return render_template('stateData/'+id+'.html')


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(hello, url_prefix='/')

    app.run()

