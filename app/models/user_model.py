import json

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import db

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.Integer(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    roles = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, phone, password, roles=["customer"]):
        self.name = name
        self.roles = json.dumps(roles)
        self.email=email
        self.phone=phone
        self.password_hash = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    # Esta funcion encuentra un usuario por su nombre de usuario
    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()





