from datetime import datetime
from app import application, db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

ma = Marshmallow(application)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    registered_date = db.Column(db.String(120))
    if_verified = db.Column(db.Boolean())
    real_name = db.Column(db.String(120))
    sex       = db.Column(db.String(120))
    minority  = db.Column(db.String(120))
    account_active  = db.Column(db.Boolean())

    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username):
        self.username = username

    def __init__(self, username, sex, registered_date):
        self.username = username
        self.sex = sex
        self.registered_date = registered_date

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class FuzzySearchRaw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(140))
    storage = db.Column(db.String(10000))

    def __init__(self, keyword):
        self.keyword = keyword

    def set_storage(self, storage):
        self.storage = storage

    def get_storage(self):
        return self.storage

    def __repr__(self):
        return '<MerchantRaw {}>'.format(self.keyword)


class MerchantQueryRaw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(140))
    storage = db.Column(db.String(20000))

    def __init__(self, keyword):
        self.keyword = keyword

    def set_storage(self, storage):
        self.storage = storage

    def get_storage(self):
        return self.storage

    def __repr__(self):
        return '<MerchantRaw {}>'.format(self.keyword)


class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complaint_body = db.Column(db.String(2000))
    expected_solution_body = db.Column(db.String(2000))
    complain_type = db.Column(db.String(140))
    complain_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    if_negotiated_by_merchant =  db.Column(db.Boolean(), default=False)
    negotiate_timestamp = db.Column(db.DateTime, index=True)
    allow_public =  db.Column(db.Boolean(), default=False)
    allow_contact_by_merchant =  db.Column(db.Boolean(), default=False)
    allow_press =  db.Column(db.Boolean(), default=False)
    item_price =  db.Column(db.String(200))
    item_model = db.Column(db.String(200))
    trade_info = db.Column(db.String(2000))
    relatedProducts = db.Column(db.String(200))
    purchase_timestamp = db.Column(db.DateTime, index=True)

    invoce_files = db.Column(db.String(2000))
    id_files = db.Column(db.String(2000))

class ComplaintSchema(ma.Schema):
    class Meta:
        model = Complaint
        # Fields to expose
        fields = ("complaint_body",
                  "expected_solution_body",
                  "complain_type",
                  "complaint_id",
                  "complain_timestamp",
                  "if_negotiated_by_merchant",
                  "negotiate_timestamp",
                  "allow_public",
                  "allow_contact_by_merchant",
                  "allow_press",
                  "item_price",
                  "item_model",
                  "trade_info",
                  "relatedProducts",
                  "invoce_files",
                  "id_files",
                  "purchase_timestamp")


    complaint_id = fields.String(attribute="id")