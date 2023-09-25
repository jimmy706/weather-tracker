from flask import Flask, request
from flask_restx import Api, Resource, fields
import logging
from clients import WeatherApiClient

logger = logging.getLogger(__name__)

api = Api()

app = Flask(__name__)
api.init_app(app)

weather_api_client = WeatherApiClient(logger)

location_model = api.model('Location', {
    "name": fields.String,
    "region": fields.String,
    "country": fields.String,
    "lat": fields.Float,
    "lon": fields.Float,
    "tz_id": fields.String,
    "localtime_epoch": fields.Integer,
    "localtime": fields.DateTime
})

forecast_condition = api.model('Forecast Condition', {
    'text': fields.String,
    'icon': fields.String,
})

hour_forecast_item = api.model('Hour Forecast Item', {
    'time': fields.DateTime,
    'temp_c': fields.Float,
    'feelslike_c': fields.Float,
    'will_it_rain': fields.Integer,
    'chance_of_rain': fields.Integer,
    'uv': fields.Integer,
    'condition': fields.Nested(forecast_condition)
})

forecast_item = api.model('Forecast Item', {
    'date': fields.Date,
    'hour': fields.List(fields.Nested(hour_forecast_item))
})

forecast_model = api.model('Forecast', {
    "forecastday": fields.List(fields.Nested(forecast_item))
})

forecast_response_model = api.model('Weather forecast response', {
    "location": fields.Nested(location_model),
    "forecast": fields.Nested(forecast_model)
})


@api.route('/api/weather/forecast')
class Weather(Resource):

    @api.doc(
        params={
            'q': 'Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name.',
            'days': 'Number of days of weather forecast. Value ranges from 1 to 14'
        })
    @api.response(200, 'Success', forecast_response_model)
    def get(self):
        q = request.args.get('q')
        days = request.args.get('days')
        json_response = weather_api_client.forcast(q, days)
        return json_response, 200
