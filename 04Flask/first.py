from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def home():
    return 'Home, sweet home!'
@my_app.route('/school')
def school():
    return 'Ah yes, when are we not here'
@my_app.route('/work')
def work():
    return 'Gots to make money'
@my_app.route('/vball')
def vball():
    return 'No pain, no gain'

if __name__ == '__main__':
    my_app.debug == True
    my_app.run()
