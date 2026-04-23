#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    products = []
    with open('products.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        })
    return products


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products_data = []

    try:
        if source == 'json':
            products_data = read_json()
        elif source == 'csv':
            products_data = read_csv()
        elif source == 'sql':
            products_data = read_sql()
        else:
            return render_template('product_display.html', error='Wrong source')

        if product_id:
            filtered_products = []
            for product in products_data:
                if str(product.get('id')) == str(product_id):
                    filtered_products.append(product)

            if not filtered_products:
                return render_template(
                    'product_display.html',
                    error='Product not found'
                )

            products_data = filtered_products

        return render_template(
            'product_display.html',
            products=products_data
        )

    except Exception:
        return render_template(
            'product_display.html',
            error='Error reading from database'
        )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
