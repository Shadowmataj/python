from ensurepip import bootstrap

from flask import Flask, render_template, redirect

from form import MyForm
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    admin_email="admin@email.com"
    admin_password="12345678"
    form = MyForm()
    if form.validate_on_submit():
        if admin_password == form.password.data and admin_email == form.email.data:
            return redirect("/success")
        else:
            return redirect("/denied")
    return render_template('login.html', form=form)

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
