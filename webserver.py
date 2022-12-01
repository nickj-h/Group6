from flask import Flask, Blueprint, render_template
from flask import Flask, request, render_template,redirect, url_for
import pickle

app = Flask(__name__)
accounts = dict()
mySearch = list()

# test account
accounts['softwareengineers'] = 'makemoney'


@app.route('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    name = ''
    pwd = ''
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        # if username does not exist
        if name not in accounts:
            return render_template('login.html', msg='Invalid Username')
        # if password invalid
        elif accounts[name] != pwd:
            return render_template('login.html', msg='Invalid Password')
        # if username and password both are correct
        elif name in accounts and accounts[name] == pwd:
            # set the homepage here
            # direct to the homepage
            #return render_template('homepage.html')
            return redirect("http://127.0.0.1:5000/", code=302)
            #return show_homepage()
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    newName = ''
    newPwd = ''
    if request.method == 'POST':
        newName = request.form['username']
        newPwd = request.form['password']
        # if username is blank
        if newName == '':
            return render_template('register.html', msg='Invalid Username!')
        # if username already in the accounts
        elif newName in accounts:
            return render_template('register.html', msg='Username Already Exists!')
        # if password is blank
        elif newName not in accounts and newPwd == '':
            return render_template('register.html', msg='Invalid Password!')
        # add new username to the accounts
        else:
            accounts[newName] = newPwd
            return render_template('register.html', msg='Successfully Signed Up!')
    return render_template('register.html')

#Need to incorporate this save function
'''
@app.route('/pythonProject/templates/homepage', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        page = request.form['save_search']
        if page not in mySearch:
            mySearch.append(page)
    return render_template('homepage.html', data=mySearch)
'''

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

@app.route('/management')
def show_management():
    return render_template('management.html')

@app.route('/business')
def show_business():
    return render_template('business.html')

@app.route('/computer')
def show_computer():
    return render_template('computer.html')

@app.route('/architecture')
def show_architecture():
    return render_template('Architecture.html')

@app.route('/life')
def show_life():
    return render_template('life.html')

@app.route('/community')
def show_community():
    return render_template('community.html')

@app.route('/construction')
def show_construction():
    return render_template('construction.html')

@app.route('/legal')
def show_legal():
    return render_template('legal.html')

@app.route('/educational')
def show_educational():
    return render_template('educational.html')

@app.route('/arts')
def show_arts():
    return render_template('arts.html')

@app.route('/healthcarepractitioners')
def show_healthcarepractitioners():
    return render_template('healthcarepractitioners.html')

@app.route('/healthcaresupport')
def show_healthcaresupport():
    return render_template('healthcaresupport.html')

@app.route('/protective')
def show_protective():
    return render_template('protective.html')

@app.route('/food')
def show_food():
    return render_template('food.html')

@app.route('/building')
def show_building():
    return render_template('building.html')

@app.route('/personal')
def show_personal():
    return render_template('personal.html')

@app.route('/sales')
def show_sales():
    return render_template('sales.html')


@app.route('/office')
def show_office():
    return render_template('office.html')

@app.route('/farming')
def show_farming():
    return render_template('farming.html')

@app.route('/installation')
def show_installation():
    return render_template('installation.html')

@app.route('/production')
def show_production():
    return render_template('production.html')

@app.route('/transportation')
def show_transportation():
    return render_template('transportation.html')


#/stateMap/main is the default map.
# upon clicking a state, javascript calls the /stateMap/id route where id is the 2-letter state code  e.g. stateMap/FL
# and flask serves the appropriate data

@app.route('/stateMap/<id>')
def show_stateMap(id):
    if id == "main":
        return render_template('stateMap.html') 
    return render_template('stateData/'+id+'.html')

'''
@app.route('/')
def app_world():
    return 'app, World!'
'''
if __name__ == '__main__':
   # app = Flask(__name__)
    #app.register_blueprint(app, url_prefix='/')

    app.run()

