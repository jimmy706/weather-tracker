import os
import requests
import urllib.parse

class WeatherApiClient:
    def __init__(self, logging):
        self.__api_key = os.environ.get("WEATHER_API_KEY")
        self.__base_url = os.environ.get("WEATHER_API_URL")
        self.__logging = logging
        
    def forcast(self, q: str, days: int):
        key = self.__api_key
        _url = self.__base_url + "/forecast.json"
        params = {"q": q, "days": days, "key": key}
        response = requests.get(_url, params=urllib.parse.urlencode(params))
        self.__logging.info('Request weather api with url: %s', response.url)
        if response.ok:
            return response.json()
        else:
            message = "Failed to call API %s, Error: %s", response.url, response.json()
            self.__logging.warning(message)
            raise Exception(message)
