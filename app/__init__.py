from flask import Flask
from app import store, models, dummy_data


app = Flask(__name__)


member_store = store.MembersStore()
post_store = store.PostsStore()
dummy_data.seed_stores(member_store, post_store)


from app import views
