from src.data_loader import fetch_weather_data
from src.data_cleaner import clean_weather_data
from src.analyzer import plot_temperature
from src.data_loader import fetch_weather_data
from src.data_cleaner import clean_weather_data
from src.feature_engineering import engineer_features, select_features
from src.analyzer import plot_temperature
from src.data_loader import fetch_weather_data
from src.data_cleaner import clean_weather_data
from src.feature_engineering import engineer_features, select_features
from src.statistics import summarize_statistics, generate_insights, missing_data_report
from src.analyzer import plot_temperature
from src.data_loader import fetch_weather_data
from src.data_cleaner import clean_weather_data
from src.feature_engineering import engineer_features
from src.statistics import summarize_statistics, generate_insights
from src.pattern_analysis import detect_trends, detect_anomalies, identify_seasonal_patterns, plot_trend_and_anomalies
from src.analyzer import plot_temperature
from src.data_transformer import remove_outliers_iqr, log_transform, standardize

# Remove outliers
featured = remove_outliers_iqr(featured, column='tavg')

# Optional: log-transform and standardize
featured = log_transform(featured, column='tavg')
featured = standardize(featured, column='tavg')

# Load and process
raw_data = fetch_weather_data("New York", "2023-01-01", "2023-12-31")
cleaned = clean_weather_data(raw_data)
featured = engineer_features(cleaned)

# Statistics
summarize_statistics(featured)
generate_insights(featured)

# Trend & Pattern Analysis
featured = detect_trends(featured, column='tavg', window=30)
seasonal = identify_seasonal_patterns(featured)
featured = detect_anomalies(featured, column='tavg', threshold=2.0)

# Plot
plot_trend_and_anomalies(featured, column='tavg')


# Load data
raw_data = fetch_weather_data(location_name="New York", start="2023-01-01", end="2023-12-31")
