#This is the webserver to handle routing for the web app

from flask import Flask, Blueprint, render_template
from flask import Flask, request, render_template, redirect, url_for
import pickle

app = Flask(__name__)
accounts = dict()
mySearch = list()


#hashmap to hold account/password combos
# test account for login
accounts['softwareengineers'] = 'makemoney'

#main page
@app.route('/', methods=['GET', 'POST'])
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
            # return render_template('homepage.html')
            return render_template('homepage.html')
            # return show_homepage()
    return render_template('login.html')


#routes to the register page
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

#Save the current page to the searches
def save_search():
    page = request.form['save_search']
    if page not in mySearch:
        mySearch.append(page)

#routes to the homepage

@app.route('/homepage')
def show_homepage():
    return render_template('homepage.html', data=mySearch)

#routes to the management page

@app.route('/management', methods=['GET', 'POST'])
def show_management():
    if request.method == 'POST':
        save_search()
    return render_template('management.html')

#routes to the business page
@app.route('/business', methods=['GET', 'POST'])
def show_business():
    if request.method == 'POST':
        save_search()
    return render_template('business.html')

#routes to the computer page
@app.route('/computer', methods=['GET', 'POST'])
def show_computer():
    if request.method == 'POST':
        save_search()
    return render_template('computer.html')

#routes to the architecture page
@app.route('/architecture', methods=['GET', 'POST'])
def show_architecture():
    if request.method == 'POST':
        save_search()
    return render_template('Architecture.html')

#routes to the life page
@app.route('/life', methods=['GET', 'POST'])
def show_life():
    if request.method == 'POST':
        save_search()
    return render_template('life.html')

#routes to the community page
@app.route('/community', methods=['GET', 'POST'])
def show_community():
    if request.method == 'POST':
        save_search()
    return render_template('community.html')

#routes to the construction page
@app.route('/construction', methods=['GET', 'POST'])
def show_construction():
    if request.method == 'POST':
        save_search()
    return render_template('construction.html')

#routes to the legal page
@app.route('/legal', methods=['GET', 'POST'])
def show_legal():
    if request.method == 'POST':
        save_search()
    return render_template('legal.html')

#routes to the educational page
@app.route('/educational', methods=['GET', 'POST'])
def show_educational():
    if request.method == 'POST':
        save_search()
    return render_template('educational.html')

#routes to the arts page
@app.route('/arts', methods=['GET', 'POST'])
def show_arts():
    if request.method == 'POST':
        save_search()
    return render_template('arts.html')

#routes to the healthcare page for practitioners
@app.route('/healthcarepractitioners', methods=['GET', 'POST'])
def show_healthcarepractitioners():
    if request.method == 'POST':
        save_search()
    return render_template('healthcarepractitioners.html')

#routes to the healthcare support page
@app.route('/healthcaresupport', methods=['GET', 'POST'])
def show_healthcaresupport():
    if request.method == 'POST':
        save_search()
    return render_template('healthcaresupport.html')

#routes to the protective page
@app.route('/protective', methods=['GET', 'POST'])
def show_protective():
    if request.method == 'POST':
        save_search()
    return render_template('protective.html')

#routes to the food page
@app.route('/food', methods=['GET', 'POST'])
def show_food():
    if request.method == 'POST':
        save_search()
    return render_template('food.html')

#routes to the building page
@app.route('/building', methods=['GET', 'POST'])
def show_building():
    if request.method == 'POST':
        save_search()
    return render_template('building.html')

#routes to the personal page
@app.route('/personal', methods=['GET', 'POST'])
def show_personal():
    if request.method == 'POST':
        save_search()
    return render_template('personal.html')

#routes to the sales page
@app.route('/sales', methods=['GET', 'POST'])
def show_sales():
    if request.method == 'POST':
        save_search()
    return render_template('sales.html')

#routes to the office page
@app.route('/office', methods=['GET', 'POST'])
def show_office():
    if request.method == 'POST':
        save_search()
    return render_template('office.html')

#routes to the farming page
@app.route('/farming', methods=['GET', 'POST'])
def show_farming():
    if request.method == 'POST':
        save_search()
    return render_template('farming.html')

#routes to the installation page
@app.route('/installation', methods=['GET', 'POST'])
def show_installation():
    if request.method == 'POST':
        save_search()
    return render_template('installation.html')

#routes to the production page
@app.route('/production', methods=['GET', 'POST'])
def show_production():
    if request.method == 'POST':
        save_search()
    return render_template('production.html')

#routes to the transportation page
@app.route('/transportation', methods=['GET', 'POST'])
def show_transportation():
    if request.method == 'POST':
        save_search()
    return render_template('transportation.html')


# /stateMap/main is the default map.
# upon clicking a state, javascript calls the /stateMap/id route where id is the 2-letter state code  e.g. stateMap/FL
# and flask serves the appropriate data

@app.route('/stateMap/<id>')
def show_stateMap(id):
    if id == "main":
        return render_template('stateMap.html')
    return render_template('stateData/' + id + '.html')


'''
@app.route('/')
def app_world():
    return 'app, World!'
'''
if __name__ == '__main__':
    # app = Flask(__name__)
    # app.register_blueprint(app, url_prefix='/')

    app.run()

# login page reference:https://codeshack.io/login-system-python-flask-mysql/
