from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import User, Post, db
from views.forms import PostForm
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest

posts_app = Blueprint("posts_app", __name__, url_prefix="/posts/")


@posts_app.route("/", methods=["GET", "DELETE"], endpoint="posts_root")
def get_root():
    if request.method == "GET":
        posts = (
            Post.query.join(User, User.id == Post.user_id)
            .add_columns(Post.id, Post.body, Post.title, User.username)
            .filter(User.is_displayed == True)
            .order_by(desc(Post.created_at))
            .all()
        )
        return render_template("posts/list.html", posts=posts)


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add_post")
def add_post():
    form = PostForm()
    form.user.choices = [(u.id, u.username) for u in User.query.all()]

    if request.method == "GET":
        return render_template("posts/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("posts/add.html", form=form), 400

    post_title = form.title.data
    post_body = form.body.data
    post_user = form.user.data
    post = Post(title=post_title, body=post_body, user_id=post_user)
    # product = Product(name=product_name, description=product_description)
    db.session.add(post)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(
            f"Coudn't create product {post_title!r}, probably such some errors. Get: {post_user}."
        )

    flash(f"Sucessfully added product {post_title}!")
    url = url_for("posts_app.posts_root")
    return redirect(url)


@posts_app.route("/<int:post_id>/update/", methods={"GET", "POST"}, endpoint="update")
def update_post(post_id: int):
    # post = Post.query.join(User, Post.user_id == User.id).add_columns(Post.id, Post.title, Post.body, Post.user_id, User.username).filter(Post.id == post_id).one_or_none()
    post = Post.query.get_or_404(post_id, f"Can't find user with #{post_id}")
    user = User.query.get_or_404(post.user_id, f"Can't find user with #{post.user_id}")

    if request.method == "GET":
        form = PostForm(title=post.title, body=post.body)
        form.user.choices = [(user.id, user.username)]
        return render_template("posts/add.html", form=form)

    form = PostForm()
    form.user.choices = [(post.user_id, user.username)]
    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    post.title = form.title.data
    post.body = form.body.data

    db.session.commit()

    flash(f"Sucessfully updated post {post.title}!")
    url = url_for("posts_app.posts_root")
    return redirect(url)


@posts_app.route("/<int:post_id>/delete/", endpoint="delete")
def delete_post(post_id:int):
    post = Post.query.get_or_404(post_id, f"Can't find user with #{post_id}")
    post_title = post.title
    db.session.delete(post)
    db.session.commit()
    flash(f"Deleted product {post_title}", "warning")
    url = url_for("posts_app.posts_root")
    return redirect(url)