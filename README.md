# clothing_api
Clothing API using flask restless where a user can order clothes, shoes and other accessories.
Flask restless is made of Flask which is a Python microframework for web development whereas restless is made of REST, REpresentational State Transfer which makes communication between computer systems on the web much easier.
And restless is a simplification of restful where there is no need to declare the routes of the application program interface (API).

In this API we create two tables using sqlalchemy, user and order.
The table user has the columns:
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
   
 The tests can be done on [Click here](Postman)
   
 Here are a few examples :
 
 POST user: http://localhost/api/user
           
       {
        "id": "NTYU88jj",
        "username": "Byakal",
        "email": "B.nim@load.lol",
        "gender": "F",
        "is_under_18":false
        }           

GET user: http://localhost/api/user
           
            {
            "email": "B.nim@load.lol",
            "gender": "F",
            "id": "NTYU88jj",
            "is_under_18": false,
            "orders": [],
            "username": "Byakal"
        }
        
POST order: http://localhost/api/order

          {
          "id": "V34455p",
          "item_selected": "clothing",
          "vendor": "klvin Kloine",
          "brand": "Z.lvine",
          "size": "XS",
          "order_date": "26/04/2019 19:11:20",
          "complete":false,
          "delivered":false,
          "delivery_date": "",
          "user_id": "NTYU88jj"
        }
       
GET order: http://localhost/api/order

            {
            "brand": "Z.lvine",
            "complete": false,
            "delivered": false,
            "delivery_date": null,
            "id": "V34455p",
            "item_selected": "clothing",
            "order_date": "2019-04-26T19:11:20",
            "orders": {
                "email": "B.nim@load.lol",
                "gender": "F",
                "id": "NTYU88jj",
                "is_under_18": false,
                "username": "Byakal"
            },
            "size": "XS",
            "user_id": "NTYU88jj",
            "vendor": "klvin Kloine"
        }
       
As you can see the table order has the detail of the table user in the column orders. Viceversa goes for user.

GET user: http://localhost/api/user
      
         {
            "email": "B.nim@load.lol",
            "gender": "F",
            "id": "NTYU88jj",
            "is_under_18": false,
            "orders": [
                {
                    "brand": "Z.lvine",
                    "complete": false,
                    "delivered": false,
                    "delivery_date": null,
                    "id": "V34455p",
                    "item_selected": "clothing",
                    "order_date": "2019-04-26T19:11:20",
                    "size": "XS",
                    "user_id": "NTYU88jj",
                    "vendor": "klvin Kloine"
                }
            ],
            "username": "Byakal"
        }
        
We can also update the details using put updating columns complete, delivered and delivery_date.

PUT order according to the oreder id: http://localhost/api/order/V34455p
                                    
                                    {
                                      "id": "V34455p",
                                      "item_selected": "clothing",
                                      "vendor": "klvin Kloine",
                                      "brand": "Z.lvine",
                                      "size": "XS",
                                      "order_date": "26/04/2019 19:11:20",
                                      "complete":true,
                                      "delivered":true,
                                      "delivery_date":"29/04/2019 12:30:00",
                                      "user_id": "NTYU88jj"
                                       }
     

