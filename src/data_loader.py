from datetime import datetime
from meteostat import Point, Daily
import pandas as pd

def fetch_weather_data(location_name="New York", lat=40.7128, lon=-74.0060, start="2023-01-01", end="2023-12-31"):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    
    location = Point(lat, lon)
    data = Daily(location, start_date, end_date)
    data = data.fetch()
    data.reset_index(inplace=True)
    data["location"] = location_name
    
    return data
