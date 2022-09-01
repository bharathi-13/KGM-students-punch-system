from flask import render_template, url_for, flash, redirect
from daily_punch import app
from daily_punch.forms import RegistrationForm, LoginForm, Daily_reportForm
from daily_punch.models import User, Post
import re

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/home", methods=['GET', 'POST'])
def home():
    form = Daily_reportForm()
    if form.validate_on_submit():
       intime = form.intime.data
       outtime = form.outtime.date
       flash('Your daily report got submitted', 'success')
       return redirect(url_for('home'))
    return render_template('home.html', title="Home", form=form)

@app.route("/about")
def about():
    return render_template('about.html', title="about")

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)