from flask import Flask, request, Response, jsonify
from flask_restx import Api, Resource
import logging
from clients import WeatherApiClient
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)
# logger.addHandler(AzureLogHandler())

api = Api()

app = Flask(__name__)
api.init_app(app)

weather_api_client = WeatherApiClient(logger)


@api.route('/api/weather/forecast')
class Weather(Resource):
    @api.doc(        
        params={
        'q': 'Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name.',
        'days': 'Number of days of weather forecast. Value ranges from 1 to 14'
    })
    def get(self):
        q = request.args.get('q')
        days = request.args.get('days')
        json_response = weather_api_client.forcast(q, days)
        return json_response, 200
