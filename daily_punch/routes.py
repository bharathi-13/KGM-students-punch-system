from flask import render_template, url_for, flash, redirect
from daily_punch import app
from daily_punch.forms import RegistrationForm, LoginForm
from daily_punch.models import User, Post

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

@app.route("/home")
def home():
    return render_template('home.html', title="Home")

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