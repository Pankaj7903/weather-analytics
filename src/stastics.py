import pandas as pd

def summarize_statistics(df):
    """
    Generate and print summary statistics for weather data.

    Parameters:
    - df (pd.DataFrame): Cleaned and feature-engineered weather DataFrame

    Returns:
    - summary_df (pd.DataFrame): Statistical summary of numerical columns
    """
    print("🔎 Summary Statistics:")
    summary_df = df.describe().T
    print(summary_df)
    return summary_df


def generate_insights(df):
    """
    Generate insights and observations from the weather data.

    Parameters:
    - df (pd.DataFrame): Feature-engineered DataFrame

    Returns:
    - insights (list): List of strings with insights
    """
    insights = []

    # Insight: Warmest and coldest day
    warmest_day = df.loc[df['tavg'].idxmax()]
    coldest_day = df.loc[df['tavg'].idxmin()]
    insights.append(f"🔥 Warmest day was on {warmest_day['time'].date()} with an average temp of {warmest_day['tavg']}°C")
    insights.append(f"❄️ Coldest day was on {coldest_day['time'].date()} with an average temp of {coldest_day['tavg']}°C")

    # Insight: Month with highest average temperature
    month_avg = df.groupby('month')['tavg'].mean()
    hottest_month = month_avg.idxmax()
    insights.append(f"📈 Hottest month on average was {hottest_month} with avg temperature of {month_avg[hottest_month]:.2f}°C")

    # Insight: Most temperature fluctuation (volatility)
    most_volatile_day = df.loc[df['temp_range'].idxmax()]
    insights.append(f"🌡️ Most volatile day was {most_volatile_day['time'].date()} with a temp range of {most_volatile_day['temp_range']}°C")

    # Insight: Weekend vs weekday average temperature
    weekend_avg = df[df['is_weekend'] == 1]['tavg'].mean()
    weekday_avg = df[df['is_weekend'] == 0]['tavg'].mean()
    insights.append(f"📅 Average weekend temperature: {weekend_avg:.2f}°C")
    insights.append(f"📅 Average weekday temperature: {weekday_avg:.2f}°C")

    print("\n🧠 Generated Insights:")
    for i in insights:
        print("-", i)

    return insights


def missing_data_report(df):
    """
    Print a report of missing values in the dataset.

    Parameters:
    - df (pd.DataFrame): Any DataFrame

    Returns:
    - pd.Series: Count of missing values per column
    """
    print("\n🧾 Missing Data Report:")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    return missing
