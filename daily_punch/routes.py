from flask import render_template, url_for, flash, redirect,request
from daily_punch import app, admin, db, bcrypt
from daily_punch.forms import RegistrationForm, LoginForm, Daily_reportForm
from daily_punch.models import User, Daily_report
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
import re

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
            flash('You got logged in', 'success')

        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    form = Daily_reportForm()
    user = User()
    if form.validate_on_submit():

       intime = datetime.strptime(str(form.intime.data), "%Y-%m-%d %H:%M:%S")
       outtime = datetime.strptime(str(form.outtime.data), "%Y-%m-%d %H:%M:%S")
       difference = outtime - intime
       sec = difference.total_seconds()
       hours = sec / (60 * 60)
       
       real_datetime = datetime.now()
       fromatted_rt = real_datetime.strftime( "%Y-%m-%d %H:%M:%S" )

       if fromatted_rt < str(outtime):
        flash('Your out time is not matching with the current time', 'danger')

       else:
        flash(f'Your daily report got submitted. Your total hours is {hours}', 'success')

        punch = Daily_report(intime=intime, outtime=outtime, hours=hours, remarks=form.discription.data, student= current_user.username)
        db.session.add(punch)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('home.html', title="Home", form=form, current_user=current_user)

@app.route("/about")
def about():
    return render_template('about.html', title="about")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None or session.get('if_logged') is None:
            return redirect('/login',code=302)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/test")
def test():
    return render_template('test.html')

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Daily_report, db.session))