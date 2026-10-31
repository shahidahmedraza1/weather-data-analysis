import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read dataset
df = pd.read_csv(r"C:\Users\shahi\Downloads\weather_datasets.csv")

# Display first few records
print("First 5 rows:")
print(df.head())

# Measure the number of rows and columns
print(df.head())
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# Dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values using mode
# Exclude Date and Condition columns

columns_to_fill = [
    col for col in df.columns
    if col not in ["Date", "Condition"]
]

for col in columns_to_fill:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Handling:")
print(df.isnull().sum())

# Convert Date column to datetime
print("Available columns:", list(df.columns))
df["Date"] = pd.to_datetime(df["Date"], format="mixed")

# Extract month
df["Month"] = df["Date"].dt.month

# Basic statistical analysis
print("\nStatistical Summary:")
print(df.describe())

# Maximum and minimum temperature
print("\nMaximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())

# Average temperature
print("Average Temperature:", df["Temperature"].mean())

# Average humidity
print("Average Humidity:", df["Humidity"].mean())



# -----------------------------------
# Temperature Trend
# -----------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    df["Date"],
    df["Temperature"],
    color="red",
    linewidth=2
)

plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)

#Humidity Trend

plt.figure(figsize=(12, 6))

plt.plot(
    df["Date"],
    df["Humidity"],
    color="green"
)

plt.title("Humidity Trend")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.grid(True)

#Temperature vs Humidity

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Temperature",
    y="Humidity",
    color="purple"
)

plt.title("Temperature vs Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")

plt.show()

# Correlation Heatmap

plt.figure(figsize=(8, 6))

correlation = df[
    ["Temperature", "Humidity", "WindSpeed"]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Weather Variables Correlation")

plt.show()


# -----------------------------------
# Monthly Average Temperature
# -----------------------------------

monthly_temperature = df.groupby("Month")["Temperature"].mean()

plt.figure(figsize=(10, 5))

monthly_temperature.plot(
    kind="bar",
    color="tomato"
)

plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")

plt.show()
