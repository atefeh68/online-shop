from sqlalchemy import *
from extentions import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String(50), unique=True ,nullable=False,index=True)
    password = Column(String(120), nullable=False,index=True)
    phone = Column(String(11), nullable=False,index=True)
    address = Column(String(50), nullable=False,index=True)