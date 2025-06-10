import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

sns.set_context("notebook", font_scale=1.2)
plt.style.use('seaborn-vibrant')

# Static + Aesthetic
def plot_temperature_trend(df):
    plt.figure(figsize=(12, 5))
    plt.plot(df['date'], df['temperature'], color='tomato', linewidth=2)
    plt.title("📈 Temperature Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Interactive Line Chart
def interactive_temperature_plot(df):
    fig = px.line(df, x='date', y='temperature', title='Interactive Temperature Trend')
    fig.update_traces(line=dict(color='crimson'))
    fig.update_layout(template='plotly_white', hovermode='x unified')
    fig.show()

def interactive_precipitation_by_month(df):
    fig = px.box(df, x='month', y='precipitation',
                 title='Monthly Precipitation Boxplot (Interactive)',
                 color='month', template='plotly_white')
    fig.update_layout(xaxis_title='Month', yaxis_title='Precipitation (mm)')
    fig.show()

def interactive_feature_correlation(df):
    fig = px.imshow(df.corr(numeric_only=True), text_auto=True,
                    title="Correlation Matrix (Interactive)", color_continuous_scale='RdBu')
    fig.show()


def plot_temperature_trend(df):
    plt.figure(figsize=(12, 5))
    plt.plot(df['date'], df['temperature'], color='red')
    plt.title("Temperature Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.show()

def plot_precipitation_box(df):
    plt.figure(figsize=(12, 5))
    sns.boxplot(x='month', y='precipitation', data=df, palette='cool')
    plt.title("Monthly Precipitation Distribution")
    plt.xticks(rotation=45)
    plt.show()

def plot_correlation_heatmap(df):
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Between Weather Metrics")
    plt.show()


plt.style.use('seaborn-vibrant')  # Global aesthetic style
sns.set_context("notebook", font_scale=1.2)

def plot_temperature_trend(df):
    plt.figure(figsize=(12, 5))
    plt.plot(df['date'], df['temperature'], color='tomato', linewidth=2)
    plt.title("📈 Temperature Trend Over Time", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_monthly_precipitation(df):
    plt.figure(figsize=(12, 6))
    order = df['month'].dropna().unique()
    sns.boxplot(x='month', y='precipitation', data=df, palette='Set2')
    plt.title("🌧️ Monthly Precipitation Distribution", fontsize=14)
    plt.xticks(rotation=45)
    plt.ylabel("Precipitation (mm)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_distribution(df, column, color='royalblue'):
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column], bins=30, kde=True, color=color)
    plt.title(f"📊 Distribution of {column.capitalize()}", fontsize=14)
    plt.xlabel(column.capitalize())
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df):
    corr = df[['temperature', 'humidity', 'wind_speed', 'precipitation']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("🔥 Correlation Between Weather Variables")
    plt.tight_layout()
    plt.show()

def plot_interactive_line(df, y_column):
    fig = px.line(df, x='date', y=y_column, title=f'Interactive {y_column.title()} Over Time',
                  labels={'date': 'Date', y_column: y_column.title()},
                  template='plotly_white')
    fig.update_traces(line_color='mediumblue', line_width=2)
    fig.show()
