from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import User, db
from views.forms.users import UserForm
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest


user_app = Blueprint("user_app", __name__, url_prefix="/user/")


@user_app.route("/", endpoint="users_list")
def show_root():
    users = User.query.filter_by(is_displayed=True).all()
    return render_template("users/user_list.html", users=users)

@user_app.route("/removed_users/", endpoint="users_removed_list")
def show_removed():
    users = User.query.filter_by(is_displayed=False).all()
    return render_template("users/user_list.html", users=users)

@user_app.route("/removed_users/<int:user_id>/comeback", endpoint="comeback_user")
def comeback_user(user_id: int):
    user = User.query.filter_by(id=user_id).first()
    user.is_displayed=True
    try:
        db.session.commit()
    except:
        db.session.rollback()
        raise BadRequest(f"Coudn't return user {user.username!r}, some errors.")
    url = url_for("user_app.users_list")
    return redirect(url)

@user_app.route("/remove_user/", methods=["GET"], endpoint="remove")
def remove_user_menu():
    if request.method == "GET":
        users = User.query.filter_by(is_displayed=True).all()
        return render_template("users/remove.html", users=users)

@user_app.route("/remove_user/<int:user_id>", methods=["GET"], endpoint="remove_userid")
def remove_user(user_id:int):
    if request.method == "GET":
        user = User.query.get_or_404(user_id, f"User #{user_id} not found")
        user.is_displayed = False
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise BadRequest(f"Coudn\'t remove user")
        users = User.query.filter_by(is_displayed=True).all()
        return render_template("users/remove.html", users=users)

@user_app.route("/add/", methods=["GET", "POST"], endpoint="add_user")
def add_user():
    form = UserForm()

    if request.method == "GET":
        return render_template("users/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("users/add.html", form=form), 400

    username = form.username.data
    user_email = form.email.data
    user = User(username=username, email=user_email)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Coudn't create user {username!r}, probably such product already exists.")

    flash(f"Sucessfully added user {username}!")
    # url = url_for("products_app.details", product_id=product.id)
    url = url_for("user_app.users_list")
    return redirect(url)