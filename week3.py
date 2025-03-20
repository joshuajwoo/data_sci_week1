import pandas as pd
import matplotlib.pyplot as plt

data_url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
pedestrian_data = pd.read_csv(data_url)
pedestrian_data.columns = pedestrian_data.columns.str.strip()
datetime_column = 'hour_beginning'
pedestrian_data[datetime_column] = pd.to_datetime(pedestrian_data[datetime_column])
pedestrian_data['Weekday_Name'] = pedestrian_data[datetime_column].dt.day_name()
weekdays_only = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
filtered_weekday_data = pedestrian_data[pedestrian_data['Weekday_Name'].isin(weekdays_only)]
weekday_pedestrian_counts = (
    filtered_weekday_data.groupby('Weekday_Name')['Pedestrians']
    .sum()
    .reindex(weekdays_only)
)
plt.figure(figsize=(10, 6))
plt.plot(weekday_pedestrian_counts.index, weekday_pedestrian_counts.values, marker='o')
plt.xlabel('Day of the Week')
plt.ylabel('Total Pedestrian Count')
plt.title('Pedestrian Counts for Weekdays (Monday to Friday)')
plt.grid(True)
plt.show()
brooklyn_bridge_2019 = pedestrian_data[
    (pedestrian_data['location'] == 'Brooklyn Bridge') &
    (pedestrian_data[datetime_column].dt.year == 2019)
]

print("Brooklyn Bridge 2019 data shape:", brooklyn_bridge_2019.shape)
unique_weather_conditions = brooklyn_bridge_2019['weather_summary'].unique()
print("Unique weather summaries:", unique_weather_conditions)
weather_one_hot = pd.get_dummies(brooklyn_bridge_2019['weather_summary'], prefix='Weather').astype(int)
brooklyn_weather_encoded = pd.concat([brooklyn_bridge_2019.reset_index(drop=True), weather_one_hot], axis=1)
correlation_matrix = brooklyn_weather_encoded.select_dtypes(include='number').corr()
print("Numeric columns in correlation matrix:", list(correlation_matrix.index))

weather_correlation_columns = weather_one_hot.columns.intersection(correlation_matrix.index)

if weather_correlation_columns.empty:
    print("No weather-related columns found in the correlation matrix.")
else:
    weather_pedestrian_correlation = (
        correlation_matrix[['Pedestrians']]
        .loc[weather_correlation_columns]
        .sort_values(by='Pedestrians', ascending=False)
    )
    print("Correlation between Weather Conditions and Pedestrian Counts (Brooklyn Bridge, 2019):")
    print(weather_pedestrian_correlation)
    plt.figure(figsize=(10, 6))
    weather_pedestrian_correlation['Pedestrians'].plot(kind='bar')
    plt.xlabel('Weather Condition (One-hot Encoded)')
    plt.ylabel('Correlation with Pedestrian Count')
    plt.title('Correlation between Weather Conditions and Pedestrian Counts (Brooklyn Bridge, 2019)')
    plt.show()

pedestrian_data['Hour_Time'] = pedestrian_data[datetime_column].dt.time

def categorize_time_of_day(time_value):
    hour_of_day = time_value.hour
    if 5 <= hour_of_day < 12:
        return 'Morning'
    elif 12 <= hour_of_day < 17:
        return 'Afternoon'
    elif 17 <= hour_of_day < 21:
        return 'Evening'
    else:
        return 'Night'

pedestrian_data['Time_Period'] = pedestrian_data['Hour_Time'].apply(categorize_time_of_day)
time_period_pedestrian_counts = pedestrian_data.groupby('Time_Period')['Pedestrians'].sum()
time_period_order = ['Morning', 'Afternoon', 'Evening', 'Night']
time_period_pedestrian_counts = time_period_pedestrian_counts.reindex(time_period_order)
plt.figure(figsize=(8, 6))
time_period_pedestrian_counts.plot(kind='bar')
plt.xlabel('Time of Day')
plt.ylabel('Total Pedestrian Count')
plt.title('Pedestrian Activity Patterns by Time of Day')
plt.show()