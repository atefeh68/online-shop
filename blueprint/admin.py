from flask import Blueprint, render_template, request, redirect, session, abort
import config

app = Blueprint('admin', __name__)

@app.before_request
def before_request():

    if  session.get('admin_login', None) is None and request.endpoint != 'admin/login' :
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
    if session.get('admin_login', None) is None:
        abort(403)
    return "dashboard"

@app.route('/admin/dashboard/product', methods=["GET"])
def product():
    if session.get('admin_login', None) is None:
        abort(403)
    return "product"