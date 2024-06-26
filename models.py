from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets 

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    DOB = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default=False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, first_name, last_name, DOB, email, password, token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    
    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User {self.email} has joined the KOC library DB!'
    
class Book(db.Model):
    id = db.Column(db.String, primary_key = True)
    IBSN = db.Column(db.String(150))
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    published_date = db.Column(db.String(25))
    category = db.Column(db.String(200))
    image = db.Column(db.String)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, IBSN, title, author, published_date, category, image, user_token, id = ''):
        self.id = self.set_id()
        self.IBSN = IBSN
        self.title = title
        self.author = author
        self.published_date = published_date
        self.category = category
        self.image = image

        self.user_token = user_token

    def __repr__(self):
        return f'The following book has been search for in the KOC club: {self.title}'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class BookSchema(ma.Schema):
    class Meta:
        fields = ['id','IBSN', 'title', 'author', 'published_date', 'category','image']

book_schema = BookSchema()
books_schema = BookSchema(many = True)

