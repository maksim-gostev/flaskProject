from flask import Flask, render_template
from flask_restx import Api

from config import ProductionConfig
from setup_db import db
from views.main.genres import genres_ns

api = Api(title="Flask Course Project 3", doc="/docs")


def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)

    @app.route('/')
    def index():
        return render_template('index.html')

    db.init_app(app)
    api.init_app(app)

    api.add_namespace(genres_ns)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()