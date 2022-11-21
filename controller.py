from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")


Accounts = {'softwareengineers': 'makemoney'}


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name = request.form['username']
    pwd = request.form['password']
    if name not in Accounts:
        return render_template('login.html', info='Invalid Username')
    else:
        if Accounts[name] != pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            # set the homepage here
            return render_template('homepage.html', name=name)


if __name__ == '__main__':
    app.run()

