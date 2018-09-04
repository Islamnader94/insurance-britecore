from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# An error occurs here while implementing the import in here, if it is imported under the if condition the tests works while heroku fails to fetsh.
# Set up the SQLAlchemy Database to be a local file 'risks.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///risks.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
from views import *
if __name__ == "__main__":
    app.run()
