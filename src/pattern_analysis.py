import pandas as pd
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt

def detect_trends(df, column='tavg', window=30):
    """
    Detects long-term trend using rolling mean.

    Parameters:
    - df (pd.DataFrame): Weather data
    - column (str): Column to analyze
    - window (int): Rolling window in days

    Returns:
    - pd.Series: Rolling mean (trend)
    """
    trend = df[column].rolling(window=window, min_periods=1).mean()
    df[f'{column}_trend'] = trend
    print(f"📈 Added '{column}_trend' using {window}-day rolling average.")
    return df

def identify_seasonal_patterns(df):
    """
    Identify monthly seasonal temperature patterns.

    Parameters:
    - df (pd.DataFrame): Weather data

    Returns:
    - pd.Series: Monthly average of temperature
    """
    seasonal = df.groupby('month')['tavg'].mean()
    print("\n🌤️ Monthly Seasonal Pattern (Avg Temp):")
    print(seasonal)
    return seasonal

def detect_anomalies(df, column='tavg', threshold=2.0):
    """
    Detect anomalies using Z-score method.

    Parameters:
    - df (pd.DataFrame): Weather data
    - column (str): Column to check
    - threshold (float): Z-score threshold

    Returns:
    - pd.DataFrame: DataFrame with anomaly column
    """
    df['z_score'] = zscore(df[column].fillna(df[column].mean()))
    df['is_anomaly'] = df['z_score'].abs() > threshold
    anomalies = df[df['is_anomaly']]
    
    print(f"\n🚨 Detected {len(anomalies)} anomalies in '{column}' using z-score threshold = {threshold}")
    return df

def plot_trend_and_anomalies(df, column='tavg'):
    """
    Plot original data, trend, and anomalies.

    Parameters:
    - df (pd.DataFrame): Weather data with 'trend' and 'anomaly' columns
    """
    plt.figure(figsize=(14,6))
    plt.plot(df['time'], df[column], label='Original', alpha=0.5)
    if f'{column}_trend' in df.columns:
        plt.plot(df['time'], df[f'{column}_trend'], label='Trend', linewidth=2)
    if 'is_anomaly' in df.columns:
        anomalies = df[df['is_anomaly']]
        plt.scatter(anomalies['time'], anomalies[column], color='red', label='Anomaly', zorder=5)
    plt.title(f"{column.capitalize()} Trend and Anomalies")
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.legend()
    plt.tight_layout()
    plt.show()
