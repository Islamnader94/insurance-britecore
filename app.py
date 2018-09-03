from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the SQLAlchemy Database to be a local file 'risks.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///risks.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)


if __name__ == "__main__":

    from views import *

    app.run(debug=True)
