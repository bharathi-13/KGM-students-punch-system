from flask import render_template, url_for, flash, redirect
from daily_punch import app
from daily_punch.forms import RegistrationForm, LoginForm, Daily_reportForm
from daily_punch.models import User, Daily_report
import re

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(student_id=form.student_id.data).first()
        if student_id and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/home", methods=['GET', 'POST'])
def home():
    form = Daily_reportForm()
    if form.validate_on_submit():
       intime = form.intime.data
       outtime = form.outtime.data
       flash('Your daily report got submitted', 'success')
       return redirect(url_for('home'))
    return render_template('home.html', title="Home", form=form)

@app.route("/about")
def about():
    return render_template('about.html', title="about")


@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)