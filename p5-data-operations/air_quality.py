import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Load the Air Quality dataset
# Replace 'AirQualityUCI.csv' with the actual file path
# Note: UCI dataset uses ; separator and , for decimals
df = pd.read_csv('AirQualityUCI.csv', sep=';', decimal=',')

# Display first few rows to understand the dataset
print("Original Dataset Preview:")
print(df.head())
print("\n")

# a. Data Cleaning
# Remove rows with missing values (NaN)
df_cleaned = df.dropna()
# Remove columns with all NaN values (e.g., unnamed columns in the dataset)
df_cleaned = df_cleaned.loc[:, df_cleaned.columns.notnull()]
# Remove rows with invalid values (e.g., CO(GT) = -200, which indicates missing data)
df_cleaned = df_cleaned[df_cleaned['CO(GT)'] != -200]
print("Cleaned Data Preview:")
print(df_cleaned.head())
print("\n")

# b. Data Integration
# Create a synthetic dataset for integration (e.g., weather data with temperature and humidity)
# For demo, create a small dataset with matching 'Date' column
weather_data = pd.DataFrame({
    # Match some dates
    'Date': df_cleaned['Date'].iloc[:len(df_cleaned)].unique()[:50],
    'Temperature': np.random.uniform(10, 30, 50),  # Random temperatures
    'Humidity': np.random.uniform(30, 80, 50)      # Random humidity
})
# Merge air quality data with weather data on 'Date'
integrated_df = pd.merge(
    df_cleaned.iloc[:50], weather_data, on='Date', how='inner')
print("Integrated Data Preview:")
print(integrated_df[['Date', 'CO(GT)', 'Temperature', 'Humidity']].head())
print("\n")

# c. Data Transformation
# Normalize numerical columns (e.g., CO(GT), NO2(GT))
scaler = StandardScaler()
numerical_cols = ['CO(GT)', 'NO2(GT)', 'NOx(GT)']
df_cleaned[[col + '_scaled' for col in numerical_cols]
           ] = scaler.fit_transform(df_cleaned[numerical_cols])
# Convert 'Date' to datetime and extract year/month for analysis
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], format='%d/%m/%Y')
df_cleaned['Year'] = df_cleaned['Date'].dt.year
df_cleaned['Month'] = df_cleaned['Date'].dt.month
print("Transformed Data Preview:")
print(df_cleaned[['Date', 'CO(GT)', 'CO(GT)_scaled', 'Year', 'Month']].head())
print("\n")

# d. Error Correcting
# Cap outliers (e.g., CO(GT) values above 99th percentile)
co_threshold = df_cleaned['CO(GT)'].quantile(0.99)
df_cleaned['CO(GT)'] = df_cleaned['CO(GT)'].clip(upper=co_threshold)
# Ensure non-negative values for pollutant concentrations
df_cleaned['CO(GT)'] = df_cleaned['CO(GT)'].clip(lower=0)
print("Error-Corrected Data Preview:")
print(df_cleaned[['CO(GT)', 'NO2(GT)']].head())
print("\n")

# e. Data Model Building
# Predict CO(GT) using other pollutants and transformed features
X = df_cleaned[['NO2(GT)_scaled', 'NOx(GT)_scaled', 'Month']]  # Features
y = df_cleaned['CO(GT)']  # Target (continuous variable)
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Model Performance (Mean Squared Error):", mse)
print("Sample Predictions:", y_pred[:5])
print("\n")
