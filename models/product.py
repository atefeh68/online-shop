from sqlalchemy import *
from extentions import db

class Product(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(50), unique=True ,nullable=False,index=True)
    description = Column(String(120), nullable=False,index=True)
    price = Column(String(11), nullable=False,index=True)
    active= Column(Integer, nullable=False,index=True)