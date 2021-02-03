from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://mohit2:mohit2@cluster0.aocc5.mongodb.net/rest-flask?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

app.run()