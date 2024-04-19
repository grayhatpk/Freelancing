# Import the necessary models and db instance

from website import models
from website import db
from website import app

# Create the tables in the database
db.create_all()
app.context