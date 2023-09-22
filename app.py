from flask import Flask, request
from flask_restx import Api, Resource
import logging
api = Api()

app = Flask(__name__)
api.init_app(app)

@api.route('/weather')
class Weather(Resource):
    @api.doc(params={'city': 'Your city'})
    def get(self):
        logging.info("Request current weather with city")
        return {'hello': 'world'}