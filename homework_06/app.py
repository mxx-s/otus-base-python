from flask import Flask, render_template
from views import info_app, user_app, posts_app
from models import db
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from os import getenv
from data import load_user_data, load_post_data


app = Flask(__name__)
app.register_blueprint(info_app)
app.register_blueprint(user_app)
app.register_blueprint(posts_app)

CSRFProtect(app)


CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")


db.init_app(app)
migrate = Migrate(app, db)

# For this run, run in cli: Flask db_tables
@app.cli.command("db_tables")
def db_tables():
    print(db.metadata.tables)


# For init data db tables, run : Flask init_db_data
@app.cli.command("init_db_data")
def init_data():
    load_user_data()
    load_post_data()


@app.get("/", endpoint="index_page")
def get_root():
    return render_template("index.html")
