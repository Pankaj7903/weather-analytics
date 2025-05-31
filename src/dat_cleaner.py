import pandas as pd

def clean_weather_data(df):
    # Fill missing values
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    
    # Convert temperature from °C to °F if needed
    if 'tavg' in df.columns:
        df['tavg_f'] = df['tavg'] * 9/5 + 32

    return df


def clean_weather_data(df, method='interpolate'):
    """
    Clean weather data by handling missing values.

    Parameters:
    - df (pd.DataFrame): Raw weather data.
    - method (str): Method to handle missing values. Options:
        'ffill', 'bfill', 'interpolate', 'drop'

    Returns:
    - pd.DataFrame: Cleaned weather data.
    """

    # Log missing value counts before cleaning
    print("Missing values before cleaning:")
    print(df.isnull().sum())

    if method == 'ffill':
        df.fillna(method='ffill', inplace=True)
    elif method == 'bfill':
        df.fillna(method='bfill', inplace=True)
    elif method == 'interpolate':
        df.interpolate(method='linear', inplace=True)
    elif method == 'drop':
        df.dropna(inplace=True)
    else:
        raise ValueError("Invalid method. Use 'ffill', 'bfill', 'interpolate', or 'drop'.")

    # After basic cleaning, fill remaining missing values (if any)
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # Log missing values after cleaning
    print("Missing values after cleaning:")
    print(df.isnull().sum())

    # Convert temperature columns (optional)
    if 'tavg' in df.columns:
        df['tavg_f'] = df['tavg'] * 9 / 5 + 32

    return df
