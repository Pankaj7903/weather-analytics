import streamlit as st
from src.data_loader import load_and_clean_data
from src.visualizer import (
    interactive_temperature_plot,
    interactive_precipitation_by_month,
    interactive_feature_correlation
)

st.set_page_config(page_title="🌤️ Weather Analytics Dashboard", layout="wide")

st.title("🌤️ Weather Analytics Dashboard")

# Load data
df = load_and_clean_data('data/raw_weather.csv')

# Sidebar options
chart = st.sidebar.selectbox(
    "Select Chart to Display",
    ("Temperature Trend", "Monthly Precipitation", "Correlation Matrix")
)

# Render selected chart
if chart == "Temperature Trend":
    st.subheader("📈 Temperature Trend Over Time")
    interactive_temperature_plot(df)

elif chart == "Monthly Precipitation":
    st.subheader("🌧️ Monthly Rainfall Box Plot")
    interactive_precipitation_by_month(df)

elif chart == "Correlation Matrix":
    st.subheader("📊 Feature Correlation Heatmap")
    interactive_feature_correlation(df)
