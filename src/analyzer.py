import matplotlib.pyplot as plt

def plot_temperature(df, location=""):
    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df['tavg'], label='Avg Temp (°C)')
    plt.title(f"Average Daily Temperature - {location}")
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
