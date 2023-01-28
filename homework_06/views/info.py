from flask import Blueprint, render_template

info_app = Blueprint('info_app', __name__, url_prefix="/about/")

ABOUT_TEXT = ['This is app for 0n (V n c Z: n = [1..10]) homework.'
        , 'Checking view in paragraph, rendering_templates and blueprint here.\
        Also, I\'m try to run first web app.'\
        'Try including bootstrap, and some css.'\
        'Sorry for my english :)',
        'London is the capital of the Great Britain.',
        'That\'s all. TY for reading, and visiting this page.'
]

@info_app.route('/', endpoint="ab")
def show_about():
    return render_template('info/about.html', about_text=ABOUT_TEXT)