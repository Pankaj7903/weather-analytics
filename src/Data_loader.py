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
import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.fillna(method='ffill')
    df = df[['date', 'temperature', 'humidity', 'wind_speed', 'precipitation']]
    df['month'] = df['date'].dt.month_name()
    return df
import pandas as pd

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    df.fillna(method='ffill', inplace=True)
    df['month'] = df['date'].dt.month_name()
    return df[['date', 'temperature', 'humidity', 'wind_speed', 'precipitation', 'month']]
