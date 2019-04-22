import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///C:\\UdemyPythonRestFlask\\Section6\\data.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'jose'

api = Api(app)

#@app.before_first_request
#def create_tables():
#    db.create_all()


#JWT creates a new endpoint /auth. username and password is sent to authenticate function. Checks if it is a valid user. (I think)
#auth endpoint returns a JWT token. Token goes into identity function to validate the user.


jwt =JWT(app, authenticate, identity)





    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
