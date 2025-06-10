def insight_temperature_trend(df):
    avg_temp = df['temperature'].mean()
    max_temp = df['temperature'].max()
    min_temp = df['temperature'].min()

    return (
        f"🌡️ Over the recorded period, the **average daily temperature** was "
        f"{avg_temp:.2f}°C. The highest recorded temperature was {max_temp:.2f}°C, "
        f"while the lowest was {min_temp:.2f}°C. This suggests a moderate climate "
        f"with occasional extremes worth investigating further."
    )

def insight_precipitation(df):
    monthly_avg = df.groupby("month")["precipitation"].mean().sort_values(ascending=False)
    wettest_month = monthly_avg.idxmax()
    driest_month = monthly_avg.idxmin()

    return (
        f"🌧️ The **wettest month** on average was **{wettest_month}**, while "
        f"**{driest_month}** was the driest. This information is critical for "
        f"seasonal planning in agriculture, infrastructure maintenance, and event scheduling."
    )

def insight_correlation(df):
    corr_temp_humidity = df['temperature'].corr(df['humidity'])
    corr_temp_wind = df['temperature'].corr(df['wind_speed'])

    return (
        f"🔗 There is a **{'positive' if corr_temp_humidity > 0 else 'negative'} correlation** "
        f"of {corr_temp_humidity:.2f} between temperature and humidity, and a correlation of "
        f"{corr_temp_wind:.2f} between temperature and wind speed. These insights help model how "
        f"weather parameters interact with each other."
    )
