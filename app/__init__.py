from flask import Flask, render_template
from flask_socketio import send

from app import config
from app.extensions.db_config import db, migrate
from app.extensions.sock_config import socketio


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    @app.get("/")
    def index():
        return render_template("index.html")

    @socketio.on("message", namespace="/mail")
    def handle_message(data):
        string = f"received message: {data}"
        send({"message": string}, namespace="/mail", broadcast=True)

    from .mod_webhook import bp as bp_webhook

    app.register_blueprint(bp_webhook())

    return app
