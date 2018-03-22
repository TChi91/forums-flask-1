from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, psycopg2


app = Flask(__name__)

folder_path = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = """sqlite:///{0}""".format(os.path.join(folder_path, "my_database.db"))
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://hekylxbdgwehkd:352fb94ac16ea338bb2a13a9570185bf058b030e7321a4036a1a861464e01384@ec2-54-197-250-121.compute-1.amazonaws.com:5432/d6v4kqaekjsfj'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import store, dummy_data

member_store = store.MembersStore()
post_store = store.PostsStore()
dummy_data.seed_stores(member_store, post_store)

from app import views
from app import api
