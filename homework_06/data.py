from jsonplaceholder_requests import users_list, post_list
from models import db, User, Post


def load_user_data():
    user = User.query.first()
    if user:
        print("Some users already exists. Skipped.")
        return
    for usr in users_list:
        user = User(username=usr.username, email=usr.email)
        db.session.add(user)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Some error:", str(e))


def load_post_data():
    post = Post.query.first()
    if post:
        print("Some posts already exists. Skipped.")
        return
    for pst in post_list:
        user = User.query.get(pst.user_id)
        post = Post(title=pst.title, body=pst.body, user=user)
        db.session.add(post)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Some error", str(e))
