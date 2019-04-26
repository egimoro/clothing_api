#A user uses a clothing app to order some clothes, shoes, accesories and brands, it includes the gender of the user

import os
from flask import Flask,jsonify,request
import flask_sqlalchemy
import flask_restless
import psycopg2 # Python extension for PostgrSQL
from flask_marshmallow import Marshmallow

# Create the clothing application and the Flask-SQLAlchemy object

app=Flask(__name__)
ma=Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('Database_URI1')
db=flask_sqlalchemy.SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Unicode,primary_key=True)
    username=db.Column(db.Unicode,unique=True)
    email=db.Column(db.Unicode,unique=True)
    gender=db.Column(db.String(1))
    is_under_18=db.Column(db.Boolean)
    
    

class Order(db.Model):
    id=db.Column(db.Unicode,primary_key=True)
    item_selected=db.Column(db.Unicode)
    vendor=db.Column(db.Unicode)
    brand=db.Column(db.Unicode)
    size=db.Column(db.Unicode)
    order_date=db.Column(db.DateTime)
    complete=db.Column(db.Boolean)
    delivered=db.Column(db.Boolean)
    delivery_date=db.Column(db.DateTime)
    user_id=db.Column(db.Unicode,db.ForeignKey('user.id'))
    orders=db.relationship('User',
    backref=db.backref('orders'))

   
db.create_all()

manager=flask_restless.APIManager(app,flask_sqlalchemy_db=db)

manager.create_api(User,methods=['GET','POST','DELETE','PUT'])
manager.create_api(Order,methods=['GET','POST','DELETE','PUT'])

class UserSchema(ma.ModelSchema):
    class Meta:
        model=User

class OrderSchema(ma.ModelSchema):
    class Meta:
        model=Order

user_schema=UserSchema()
order_schema=OrderSchema()


if __name__ == "__main__":
    app.run(debug=True)



