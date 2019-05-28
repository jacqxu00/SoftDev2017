from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

@my_app.route('/')
def root():
    u = urllib2.urlopen('http://api.walmartlabs.com/v1/paginated/items?brand=adidas&apiKey=zdfzqdrtacehddb6sk26gecx')
    data = u.read()
    ans = json.loads(data)
    return render_template('display.html', info = ans)
    
    
@my_app.route('/nasa')
def nasa():
    u = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=YN1S8hSoEYFRaMKTsQQYKdjpv5msA6KDpqbIEA5p')
    data = u.read()
    ans = json.loads(data)
    return render_template('orig.html', info = ans)
 
 
if __name__ == '__main__':
    my_app.debug = True
    my_app.run()