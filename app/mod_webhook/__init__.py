from flask import Blueprint


def bp():
    _bp = Blueprint("webhook", __name__, url_prefix="/webhook")

    from .routes import bp

    _bp.register_blueprint(bp)

    return _bp
