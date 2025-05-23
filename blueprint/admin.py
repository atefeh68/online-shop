from flask import Blueprint, render_template, request, redirect, session, abort, url_for
import config
from extentions import db
from models.product import Product

app = Blueprint('admin', __name__)

@app.before_request
def before_request():

    if  session.get('admin_login', None) is None and request.endpoint != 'admin.login' :
        abort(403)

@app.route('/admin/login',methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
            session['admin_login'] = username
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")

    else:
        return render_template("admin/login.html")

@app.route('/admin/dashboard', methods=["GET"])
def dashboard():
    return render_template("admin/dashboard.html")

@app.route('/admin/dashboard/products', methods=["GET","POST"])
def product():
    if request.method == "GET":
       products = Product.query.all()
       return render_template("admin/products.html",products=products)
    else:
        name = request.form.get('name', None)
        description = request.form.get('description', None)
        price = request.form.get('price', None)
        active = request.form.get('active', None)
        print(name)
        p=Product(name=name, description=description, price=price)
        if active is None:
            p.active = 0
        else:
            p.active = 1

        db.session.add(p)
        db.session.commit()

        return "done"

@app.route('/admin/dashboard/edit-product/<id>', methods=["GET","POST"])
def edit_product(id):
    products = Product.query.filter(Product.id == id).first_or_404()

    if request.method == "GET":
       return render_template("admin/edit-product.html",products=products)
    else:
        name = request.form.get('name', None)
        description = request.form.get('description', None)
        price = request.form.get('price', None)
        active = request.form.get('active', None)

        products.name = name
        products.description = description
        products.price = price
        products.active = active

        if active is None:
            products.active = 0
        else:
            products.active = 1


        db.session.commit()

        return redirect(url_for("admin.product" ,id=id))



