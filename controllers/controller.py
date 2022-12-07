from flask import render_template
from app import app
from models.items import orders


@app.route('/')
def index():
    return render_template('index.html', title="Our Book Store", orders=orders)

@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', title="This is your order", order = orders[int(index)])