from app.ext import init_ext
from app.config import init_app
from app.views import init_blue
from flask import Flask

def create_app():
    app=Flask(__name__)#,template_folder='../templates' static_folder=''

    init_app(app)

    init_ext(app)

    init_blue(app)

    return app