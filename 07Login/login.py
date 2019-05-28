# Jackie Xu and William Soe
# SoftDev Pd9
# HW07 Login
# 10.04.17

from flask import Flask, render_template, request, session, redirect
import os

# setup and set standard username and password for now
my_app = Flask (__name__)
user = 'hello'
pw = 'pass'
my_app.secret_key = os.urandom(100)

#root route: if in session render welcome page, else render login page
@my_app.route('/')
def root():
    if 'user' in session:
        return render_template("enter.html", username = session['user'])
    else:
        return render_template("form.html")

#form route: after login if user and pw correct render welcome page, else render failed login page
@my_app.route('/login', methods = ['POST'])
def form():
    if request.form['username']==user and request.form['password']==pw:
        session['user'] = request.form['username']
        return render_template("enter.html", username = request.form['username'])
    else:        
        return render_template("fail.html", user = request.form['username'], pw = request.form['password']) 

#logout route: remove user from session and display logout message
@my_app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
