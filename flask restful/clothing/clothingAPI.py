import os
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api


app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI2')


class User(db.Model):
    id = db.Column(db.Unicode, primary_key=True)
    username = db.Column(db.Unicode, unique=True)
    email = db.Column(db.Unicode, unique=True)
    gender = db.Column(db.String(1))
    is_under_18 = db.Column(db.Boolean)


class Order(db.Model):
    id = db.Column(db.Unicode, primary_key=True)
    item_selected = db.Column(db.Unicode)
    vendor = db.Column(db.Unicode)
    brand = db.Column(db.Unicode)
    size = db.Column(db.String(3))
    order_date = db.Column(db.DateTime)
    complete = db.Column(db.Boolean)
    delivered = db.Column(db.Boolean)
    delivery_date = db.Column(db.DateTime)
    orders = db.relationship('User', backref='orders')
    user_id = db.Column(db.Unicode, db.ForeignKey("user.id"))


db.create_all()


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order


user_schema = UserSchema() 
user_schemas = UserSchema(many=True)

order_schema = OrderSchema()
order_schemas = OrderSchema(many=True)


class UserList(Resource):
    def get(self):
        users = User.query.all()
        result = user_schemas.dump(users)
        return {'All users': result.data}
    
    def post(self):
        data = request.get_json()
        new_user = User(id=data['id'], 
                        username=data['username'], 
                        email=data['email'], 
                        gender=data['gender'], is_under_18=data['is_under_18'])  

        db.session.add(new_user)
        db.session.commit()

        result = user_schema.dump(new_user)

        return result, 201


class User_(Resource):

    def get(self, id):
        user = User.query.get(id)
        if user is not None:
            result = user_schema.dump(user)
            return result
        else:
            abort(404, "User not found") 
      
    def put(self, id): 
        user = User.query.get(id)
        
        if user is not None:
            user.username = request.json.get('username', user.username)
            user.email = request.json.get('email', user.email)
            user.gender = request.json.get('gender', user.gender)
            user.is_under_18 = request.json.get('is_under_18',
                                                user.is_under_18)
            result = user_schema.dump(user)
            db.session.commit()
        else:
            abort(404, "User not found")
 
        return {'User updated': result.data}

    def delete(self, id):
        user = User.query.get(id)

        if user is not None:
            db.session.delete(user)
            db.session.commit()
        
        else:
            abort(404, "User not found")
        return {'User has been deleted'}


class Order_(Resource):
    def get(self, id):
        order = Order.query.get(id)
        if order is not None:
            result = order_schema.dump(order)
            return {'Order selected': result}
        else:
            abort(404, "Order not found") 

    def put(self, id): 
        order = Order.query.get(id)
        if order is not None:
            order.item_selected = request.json.get('item_selected', 
                                                   order.item_selected)
            order.vendor = request.json.get('vendor', order.vendor)
            order.size = request.json.get('size', order.size)
            order.order_date = request.json.get('order_date', order.order_date)
            order.complete = request.json.get('complete', order.complete)
            order.delivered = request.json.get('delivered', order.delivered)
            order.delivery_date = request.json.get('delivery_date', 
                                                   order.delivery_date)
            order.brand = request.json.get('brand', order.brand)
            order.vendor = request.json.get('vendor', order.vendor)
            order.user_id = request.json.get('user_id', order.user_id)
            result = order_schema.dump(order)
            return {'Order updated': result.data}

        else:
            abort(404, "Order not found") 
    
    def delete(self, id):
        order = Order.query.get(id)

        if order is not None:
            db.session.delete(order)
            db.session.commit()

        else:
            abort(404, "Order not found")
        return {'Order has been deleted'}


class OrderList(Resource):
    def get(self):
        order = Order.query.all()
        result = order_schemas.dump(order)
        return {'Orders': result.data} 
    
    def post(self):
        data = request.get_json()
        new_order = Order(id=data['id'], 
                          item_selected=data['item_selected'], 
                          vendor=data['vendor'], 
                          brand=data['brand'], size=data['size'],  
                          order_date=data['order_date'], 
                          complete=data['complete'], delivered=data['delivered'],
                          delivery_date=data['delivery_date'],
                          user_id=data['user_id'])  
 
        db.session.add(new_order)
        db.session.commit()

        result = order_schema.dump(new_order)

        return result, 201 


errors = {
    'UserAlreadyExistsError': { 
        'message': 'A user with that username already exists.',
        'status': 409,

    },
    'ResourceDoesNotExist': {
        'message': 'A resource with that ID no longer exists.',
        'status': 410,
        'extra': 'Any extra information you want.',
    },
    'ResourceBaseError': {
        'message': 'Internal server error',
        'status': 500,
        
    },
    'BadRequestError': {
        'message': 'Missing required parameters.',
        'status': 400,
    },
    

}  


api = Api(app, errors=errors, catch_all_404s=True)

                
api.add_resource(UserList, '/users')
api.add_resource(User_, '/users/<string:id>')
api.add_resource(OrderList, '/orders')
api.add_resource(Order_, '/orders/<string:id>')
   
if __name__ == "__main__":
    app.run(debug=True)

