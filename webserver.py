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

@hello.route('community')
def show_community():
    return render_template('community.html')

@hello.route('construction')
def show_construction():
    return render_template('construction.html')

@hello.route('legal')
def show_legal():
    return render_template('legal.html')

@hello.route('educational')
def show_educational():
    return render_template('educational.html')

@hello.route('arts')
def show_arts():
    return render_template('arts.html')

@hello.route('healthcarepractitioners')
def show_healthcarepractitioners():
    return render_template('healthcarepractitioners.html')

@hello.route('healthcaresupport')
def show_healthcaresupport():
    return render_template('healthcaresupport.html')

@hello.route('protective')
def show_protective():
    return render_template('protective.html')

@hello.route('food')
def show_food():
    return render_template('food.html')

@hello.route('building')
def show_building():
    return render_template('building.html')

@hello.route('personal')
def show_personal():
    return render_template('personal.html')

@hello.route('sales')
def show_sales():
    return render_template('sales.html')


@hello.route('office')
def show_office():
    return render_template('office.html')

@hello.route('farming')
def show_farming():
    return render_template('farming.html')

@hello.route('installation')
def show_installation():
    return render_template('installation.html')

@hello.route('production')
def show_production():
    return render_template('production.html')

@hello.route('transportation')
def show_transportation():
    return render_template('transportation.html')


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

