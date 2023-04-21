import time
from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
view_metric = Counter('view', 'Product_view', ['product'])
buy_metric = Counter('buy', 'Product_buy', ['product'])

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/view/<id>')
def view_produt(id):
    view_metric.labels(product=id).inc()
    return '<h1>Hello you viewed product</h2>'

@app.route('/buy/<id>')
def buy_produt(id):
    buy_metric.labels(product=id).inc()
    return '<h1>Hello you buy product</h2>'

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)