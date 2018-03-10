from flask import jsonify, request, render_template, abort
from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/add", methods=["POST"])
def topic_create():
    request_data = request.get_json()
    new_post = models.Post(request_data["title"], request_data["content"])
    post_store.add(new_post)
    return jsonify(new_post.__dict__())


@app.route("/api/topic/view/<int:id>", methods=["VIEW"])
def topicView(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)

    return jsonify(post.__dict__())


@app.route("/api/topic/update/<int:id>", methods=["PUT"])
def topicUpdate(id):
    request_data = request.get_json()
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)

    post.title = request_data["title"]
    post.content = request_data["content"]
    post_store.update(post)

    return jsonify(post.__dict__())


@app.route("/api/topic/delete/<int:id>", methods=["DELETE"])
def topicDelete(id):
    try:
        post_store.delete(id)
    except ValueError:
        abort(404)

    return topic_get_all()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
