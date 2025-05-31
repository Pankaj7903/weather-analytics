import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_temperature_distribution(df):
    """Plot distribution of average daily temperature."""
    plt.figure(figsize=(10, 5))
    sns.histplot(df['tavg'].dropna(), bins=30, kde=True, color='skyblue')
    plt.title("📊 Distribution of Average Temperature")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def plot_monthly_avg_temperature(df):
    """Plot average temperature per month."""
    monthly_avg = df.groupby('month')['tavg'].mean()
    plt.figure(figsize=(10, 5))
    sns.barplot(x=monthly_avg.index, y=monthly_avg.values, palette='coolwarm')
    plt.title("🌡️ Monthly Average Temperature")
    plt.xlabel("Month")
    plt.ylabel("Avg Temperature (°C)")
    plt.tight_layout()
    plt.show()

def plot_temp_trend(df):
    """Line plot of daily average temperature and its trend (if exists)."""
    plt.figure(figsize=(14, 5))
    plt.plot(df['time'], df['tavg'], label='Average Temp', alpha=0.6)
    if 'tavg_trend' in df.columns:
        plt.plot(df['time'], df['tavg_trend'], label='Trend', linewidth=2, color='red')
    plt.title("📈 Daily Temperature and Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_anomalies(df):
    """Scatter plot highlighting temperature anomalies."""
    if 'is_anomaly' not in df.columns:
        print("❗ No 'is_anomaly' column found.")
        return
    plt.figure(figsize=(14, 5))
    normal = df[df['is_anomaly'] == False]
    anomalies = df[df['is_anomaly'] == True]
    plt.plot(normal['time'], normal['tavg'], label='Normal', alpha=0.5)
    plt.scatter(anomalies['time'], anomalies['tavg'], color='red', label='Anomaly')
    plt.title("🚨 Temperature Anomalies")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.tight_layout()
    plt.show()
