from views import DataParcel
from flask import Blueprint
from flask_restful import Api, Resource

superv1= Blueprint("apiv1", __name__, url_prefix="/api/v1")
api= Api(superv1)

api.add_resource(DataParcel, "/parcel")