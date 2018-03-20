from flask import jsonify, request, abort
from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/add", methods=["POST"])
def topic_create():
    request_data = request.get_json()
    try:
        new_post = models.Post(title=request_data["title"], content=request_data["content"])
        post_store.add(new_post)
        result = jsonify(new_post.as_dict())
    except KeyError:
        result = abort(400, f"Couldn't parse the request data !")

    return result


@app.route("/api/topic/show/<int:id>", methods=["GET"])
def topicView(id):
    post = post_store.get_by_id(id)
    try:
        result = jsonify(post.__dict__())
    except AttributeError:
        result = abort(404, f"topic with id: {id} doesn't exist")

    return result


@app.route("/api/topic/update/<int:id>", methods=["PUT"])
def topicUpdate(id):
    request_data = request.get_json()
    post = post_store.get_by_id(id)
    try:
        post.title = request_data["title"]
        post.content = request_data["content"]
        post_store.update(post)
        result = jsonify(post.__dict__())
    except AttributeError:
        result = abort(404, f"topic with id: {id} doesn't exist")
    except KeyError:
        result = abort(400, f"Couldn't parse the request data !")

    return result


@app.route("/api/topic/delete/<int:id>", methods=["DELETE"])
def topicDelete(id):
    try:
        result = post_store.delete(id)
        result = jsonify("topic with id " + str(id) + " deleted")
    except ValueError:
        result = abort(404, f"topic with id: {id} doesn't exist")

    return result


@app.errorhandler(400)
def bad_request(error):
    return jsonify(message = error.description)
