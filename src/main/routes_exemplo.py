from flask import Blueprint, jsonify

exemplo_bp = Blueprint(name="exemplo", import_name=__name__, url_prefix=None)


@exemplo_bp.route("/", methods=["GET"])
def hello():
    return jsonify("Hello from Flask")


@exemplo_bp.route("/erro", methods=["GET"])
def erro():
    x = 1 / 0  # noqa
    return jsonify("This is a route with internal error")
