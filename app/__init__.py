from flask import Flask, Blueprint
from .api.v1 import superv1


def create_app():
	app= Flask(__name__)
	app.register_blueprint(superv1)

	return app


