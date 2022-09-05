from datetime import datetime
from daily_punch import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    batch = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    report = db.relationship('Daily_report', backref='author', lazy=True)
    student_id = db.Column(db.String(8), nullable=False, unique=True, )

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.batch}', '{self.student_id}')"


class Daily_report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intime = db.Column()

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"