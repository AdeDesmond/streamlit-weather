import os
from dotenv import load_dotenv
import requests


load_dotenv()

key = os.getenv("API_KEY")



def get_data(place, forecast_days= None, kind=None):
    API_URL=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={key}"
    response = requests.get(API_URL)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]   
    return filtered_data



