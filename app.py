from flask import Flask
from database.db import initialize_db
from resource.movie import movies

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://mohit2:mohit2@cluster0.aocc5.mongodb.net/rest-flask?retryWrites=true&w=majority'
}

initialize_db(app)
app.register_blueprint(movies)

app.run()