import pandas as pd

def engineer_features(df):
    """
    Perform feature engineering on cleaned weather data.

    Parameters:
    - df (pd.DataFrame): Cleaned weather DataFrame with standard columns

    Returns:
    - pd.DataFrame: DataFrame with new engineered features
    """
    
    # Ensure date is datetime type
    df['time'] = pd.to_datetime(df['time'])
    
    # Create temperature range feature (if available)
    if 'tmin' in df.columns and 'tmax' in df.columns:
        df['temp_range'] = df['tmax'] - df['tmin']
    
    # Rolling 7-day average of temperature
    if 'tavg' in df.columns:
        df['tavg_rolling_7'] = df['tavg'].rolling(window=7, min_periods=1).mean()

    # Month and day features
    df['month'] = df['time'].dt.month
    df['dayofweek'] = df['time'].dt.dayofweek

    # Flag for weekends
    df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)

    # Example normalization (optional)
    # df['tavg_norm'] = (df['tavg'] - df['tavg'].mean()) / df['tavg'].std()

    return df

def select_features(df, feature_list=None):
    """
    Select a subset of features for analysis or modeling.

    Parameters:
    - df (pd.DataFrame): DataFrame with all features
    - feature_list (list): List of column names to keep. If None, keep all.

    Returns:
    - pd.DataFrame: Filtered DataFrame
    """
    if feature_list is None:
        return df
    else:
        return df[feature_list]

def validate_dataframe(df, required_columns):
    """
    Validates the presence of required columns and consistent data types.

    Parameters:
    - df (pd.DataFrame): DataFrame to validate
    - required_columns (list): List of required column names

    Raises:
    - ValueError if any column is missing or has the wrong type
    """
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    if not pd.api.types.is_datetime64_any_dtype(df['time']):
        raise TypeError("Column 'time' must be of datetime type")

    if df.isnull().all(axis=1).any():
        print("Warning: Some rows contain all null values and may be dropped.")

def engineer_features(df):
    """
    Perform feature engineering on cleaned weather data.
    Ensures data consistency and integrity.

    Parameters:
    - df (pd.DataFrame): Cleaned DataFrame

    Returns:
    - pd.DataFrame: DataFrame with new features added
    """

    # Ensure required columns exist
    required_columns = ['time', 'tavg', 'tmin', 'tmax']
    validate_dataframe(df, required_columns)

    df = df.copy()

    # Ensure 'time' column is datetime
    df['time'] = pd.to_datetime(df['time'])

    # Feature: temperature range
    df['temp_range'] = df['tmax'] - df['tmin']

    # Feature: rolling average
    df['tavg_rolling_7'] = df['tavg'].rolling(window=7, min_periods=1).mean()

    # Temporal features
    df['month'] = df['time'].dt.month
    df['dayofweek'] = df['time'].dt.dayofweek
    df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)

    # Final NaN check after engineering
    if df[['temp_range', 'tavg_rolling_7']].isnull().any().any():
        print("Warning: NaN values found in engineered features. Consider reviewing input data.")

    return df

def select_features(df, feature_list=None):
    """
    Select specific features from the DataFrame.

    Parameters:
    - df (pd.DataFrame): DataFrame to filter
    - feature_list (list): Optional list of columns to select

    Returns:
    - pd.DataFrame: Filtered DataFrame
    """
    if feature_list is None:
        return df
    else:
        missing = [col for col in feature_list if col not in df.columns]
        if missing:
            raise ValueError(f"Cannot select missing features: {missing}")
        return df[feature_list]
