# clothing_api
Clothing API using flask rest where a user can order clothes, shoes and other accessories. Flask which is a Python microframework for web development whereas rest is made of REST, REpresentational State Transfer which makes communication between computer systems on the web much easier using the application program interface (API).
In this API we create two tables using sqlalchemy, user and order. The table user has the columns:
id: the identification code of the user
username: the username of the user
email: the email of the user
gender: the gender of the user (M or F)
is_under_18: a boolean whether the user is over 18 or not
While the table order has the columns:
id: the identification of the order
item_selected: the item selected clothing, shoes etc.
vendor: store where the item has been orderedfrom
brand: brand of the item
size: size of the item
order_date: date of the order
complete: a boolean whether the order is complete or not
delivered: a boolean whether the order has been delivered or not
delivery_date: date of the delivery
user_id: id reference to the user
orders: relationship between the two tables user and order
The operations that can be done for the api are:
GET: retrieve data from the table
POST: create new data on the table
DELETE: delete selected data from the table
PUT: update the table
The tests can be done on Postman or with the Swagger UI integration in flask restplus
