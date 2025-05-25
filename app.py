from flask import Flask, render_template, request, redirect, url_for
from entities.product import Product

app = Flask(__name__)
products = {}  # Dicionário para armazenar múltiplos produtos

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip().lower()
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        if name in products:
            products[name].add_products(quantity)
        else:
            products[name] = Product(name, price, quantity)

        if 'add_another' in request.form:
            return redirect(url_for('register'))
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/view')
def view():
    total_items = sum(p.quantity for p in products.values())
    total_value = sum(p.total_value_in_stock() for p in products.values())
    return render_template('view.html', products=products, total_items=total_items, total_value=total_value)

@app.route('/add', methods=['GET', 'POST'])
def add():
    message = ""
    if request.method == 'POST':
        name = request.form['name'].strip().lower()
        amount = int(request.form['amount'])

        if name in products:
            products[name].add_products(amount)
            return redirect(url_for('home'))
        else:
            message = f"Produto '{name}' não encontrado. <a href='{url_for('register')}'>Cadastrar produto</a>"

    return render_template('add.html', message=message)

@app.route('/remove', methods=['GET', 'POST'])
def remove():
    message = ""
    if request.method == 'POST':
        name = request.form['name'].strip().lower()
        amount = int(request.form['amount'])

        if name not in products:
            message = f"Produto '{name}' não encontrado."
        elif amount > products[name].quantity:
            message = f"Quantidade insuficiente no estoque para '{name}'."
        else:
            products[name].remove_products(amount)
            return redirect(url_for('home'))

    return render_template('remove.html', message=message)

@app.route('/update_name', methods=['GET', 'POST'])
def update_name():
    message = ""
    if request.method == 'POST':
        current_name = request.form['current_name'].strip().lower()
        new_name = request.form['new_name'].strip().lower()

        if current_name in products:
            products[new_name] = products.pop(current_name)
            products[new_name].update_name(new_name)
            return redirect(url_for('home'))
        else:
            message = f"Produto '{current_name}' não encontrado."

    return render_template('update_name.html', message=message)

@app.route('/update_price', methods=['GET', 'POST'])
def update_price():
    message = ""
    if request.method == 'POST':
        name = request.form['name'].strip().lower()
        price = float(request.form['price'])

        if name in products:
            products[name].update_price(price)
            return redirect(url_for('home'))
        else:
            message = f"Produto '{name}' não encontrado."

    return render_template('update_price.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
