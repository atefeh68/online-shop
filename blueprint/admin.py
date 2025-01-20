from flask import Blueprint, render_template, request, redirect
import config

app = Blueprint('admin', __name__)
@app.route('/admin/login',methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")

    else:
        return render_template("admin/login.html")