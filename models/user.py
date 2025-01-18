from sqlalchemy import *
from extentions import db

class User(db.models):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)