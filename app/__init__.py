from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

folder_path = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import store, dummy_data

member_store = store.MembersStore()
post_store = store.PostsStore()
#dummy_data.seed_stores(member_store, post_store)

from app import views
from app import api
