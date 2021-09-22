import datetime
from random import seed, randrange
from decimal import Decimal
from app import db
from werkzeug.security import check_password_hash, generate_password_hash


class Client(db.Model):
    id = db.Column(db.Numeric(5), primary_key=True, autoincrement=False)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    pesel = db.Column(db.Numeric(11), unique=True)
    passport_no = db.Column(db.String(10))
    st_class = db.Column(db.String)
    subscriptions = db.relationship('Subscription', backref='client', lazy=True)

    def __init__(self, name, surname, pesel, passport_no, st_class):
        seed()
        self.id = Decimal(randrange(100000))
        self.name = name
        self.surname = surname
        self.pesel = pesel
        self.passport_no = passport_no
        self.st_class = st_class

    def new_id(self):
        self.id = Decimal(randrange(100000))


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Numeric(10), db.ForeignKey('client.id'), nullable=False)
    date_since = db.Column(db.Date, nullable=False)
    date_due = db.Column(db.Date, nullable=False)
    datetime_last_used = db.Column(db.DateTime)
    type = db.Column(db.Integer, nullable=False)
    payments = db.relationship('Payment', backref='subscription', lazy=True)


class SubscriptionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    length = db.Column(db.Date)
    price = db.Column(db.Numeric(4, 2), nullable=False)


class StudentClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    profile = db.Column(db.String)
    head_teacher = db.Column(db.String)


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)
    amount = db.Column(db.Numeric(4, 2), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String, nullable=False)
    #    role = db.Column(db.Integer, db.ForeignKey('userrole.id'), nullable=False)
    name = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    last_login = db.Column(db.DateTime)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

# class UserRole(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String, nullable=False)
#    users = db.relationship('User', backref='userrole', lazy=True)
