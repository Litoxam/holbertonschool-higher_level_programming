#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)

    items = data.get('items', [])

    return render_template('items.html', items=items)
@app.route('/products')
def products():
    # example : /products?source=json&id=2
    # source = json
    source = request.args.get("source")
    # product_id = 2
    product_id = request.args.get("id")

    if source == "json":
        with open('products.json', 'r') as f:
            products = json.load(f)

    elif source == "csv":
        with open('products.csv', 'r') as f:
            products = list(csv.DictReader(f))

    else:
        return render_template("product_display.html",  products=[],  error="Wrong source")
    if product_id:
        filtered_products = []

        for product in products:
            if str(product["id"]) == product_id:
                filtered_products.append(product)

        if not filtered_products:
            return render_template("product_display.html", products=[], error="Product not found")

        products = filtered_products

    return render_template("product_display.html",products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)