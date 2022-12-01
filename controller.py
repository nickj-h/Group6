from flask import Flask, request, render_template, url_for
import pickle

# a dictionary for storing accounts
accounts = dict()
mySearch = list()

app = Flask(__name__)


#  first, return a login page
@app.route('/')
def create_page():
    return render_template("login.html")


# test account
accounts['softwareengineers'] = 'makemoney'


@app.route('/pythonProject/templates/register', methods=['GET', 'POST'])
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


@app.route('/pythonProject/templates/login', methods=['GET', 'POST'])
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
            return render_template('homepage.html')
    return render_template('login.html')


@app.route('/pythonProject/templates/homepage', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        page = request.form['save_search']
        if page not in mySearch:
            mySearch.append(page)
    return render_template('homepage.html', data=mySearch)


if __name__ == '__main__':
    app.run()

# reference:https://codeshack.io/login-system-python-flask-mysql/
