from flask import render_template, request, redirect, url_for, abort, jsonify
from app import models
from app import app, member_store, post_store


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())


@app.route("/topic_add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))

    else:
        return render_template("topic_add.html")


@app.route("/topic_view/<int:id>")
def topic_view(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404, "Couldn't find this topic id !")

    return render_template("topic_view.html", post = post)


@app.route("/topic_edit/<int:id>", methods = ["GET", "POST"])
def topic_edit(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)

    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        post_store.update(post)
        return redirect(url_for("home"))

    elif request.method == "GET":
        return render_template("topic_edit.html", post = post)


@app.route("/topic_delete/<int:id>")
def topic_delete(id):
    try:
        post_store.delete(id)
    except ValueError:
        abort(404)

    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', message = error.description)
