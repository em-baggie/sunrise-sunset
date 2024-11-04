# Please see README.md for how to install additional modules
import requests

def get_coords(city, country):
    # define endpoint and send get request to API
    endpoint = f"https://photon.komoot.io/api/?q={city}, {country}&osm_tag=place:city&limit=1"
    response = requests.get(endpoint)
    # parse response to json object
    data = response.json()
    # retrieve latitude and longitude variables from json object response
    long = float(data["features"][0]['geometry']['coordinates'][0])
    lat = float(data["features"][0]['geometry']['coordinates'][1])
    # define coordinates dictionary and return this
    coords = {"latitude": lat, "longitude": long}
    return coords

def get_sun(date, long, lat):
    # define endpoint and send get request to API
    endpoint = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={long}&date={date}"
    response = requests.get(endpoint)
    # parse response to json object
    data = response.json()
    # retrieve sunrise and sunset variables from json object response
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    # define sunrise/sunset times dictionary and return this
    sun = {"sunrise": sunrise, "sunset": sunset}
    return sun