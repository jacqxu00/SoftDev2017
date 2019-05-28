# Jackie Xu
# SoftDev Pd9
# HW06 Echo
# 10.02.17

from flask import Flask, render_template, request

my_app = Flask (__name__)

@my_app.route('/')
def root():
    return render_template("form.html")

@my_app.route('/form')
def form():
    return render_template("enter.html", username = request.args['username'])

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
