Below is the Python code to perform the specified operations on the Air Quality dataset using Pandas, NumPy, and Scikit-learn, tailored for a beginner in data science with a development background. I'll use the UCI Air Quality dataset (available from the UCI Machine Learning Repository), which includes measurements like CO, NO2, O3, etc., from sensors. After the code, I'll provide a notes/cheatsheet summarizing the key concepts and functions for these operations.
Python Code for Air Quality Dataset Operations
python

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
    'Date': df_cleaned['Date'].iloc[:len(df_cleaned)].unique()[:50],  # Match some dates
    'Temperature': np.random.uniform(10, 30, 50),  # Random temperatures
    'Humidity': np.random.uniform(30, 80, 50)      # Random humidity
})
# Merge air quality data with weather data on 'Date'
integrated_df = pd.merge(df_cleaned.iloc[:50], weather_data, on='Date', how='inner')
print("Integrated Data Preview:")
print(integrated_df[['Date', 'CO(GT)', 'Temperature', 'Humidity']].head())
print("\n")

# c. Data Transformation
# Normalize numerical columns (e.g., CO(GT), NO2(GT))
scaler = StandardScaler()
numerical_cols = ['CO(GT)', 'NO2(GT)', 'NOx(GT)']
df_cleaned[[col + '_scaled' for col in numerical_cols]] = scaler.fit_transform(df_cleaned[numerical_cols])
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Model Performance (Mean Squared Error):", mse)
print("Sample Predictions:", y_pred[:5])
print("\n")

Notes/Cheatsheet for Assignment 2
Dataset Overview

    Air Quality Dataset: UCI Air Quality dataset with columns like Date, Time, CO(GT), NO2(GT), NOx(GT), O3, etc., representing pollutant concentrations.
    Source: UCI Machine Learning Repository (search “Air Quality UCI”).
    Format: CSV with ; separator, , for decimals, and missing values marked as -200.
    Key Columns:
        CO(GT): Carbon monoxide concentration.
        NO2(GT), NOx(GT): Nitrogen dioxide and oxides.
        Date, Time: Temporal data.

Key Libraries

    Pandas: Data manipulation (pip install pandas).
    NumPy: Numerical operations (pip install numpy).
    Scikit-learn: Machine learning and preprocessing (pip install scikit-learn).
    Import:
    python

    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_squared_error

Operations and Functions

    Data Cleaning
        What: Remove or handle missing values, invalid data, or irrelevant columns.
        Why: Ensure data quality for accurate analysis/modeling.
        Code:
            Drop NaN: df.dropna()
            Drop null columns: df.loc[:, df.columns.notnull()]
            Filter invalid values: df[df['col'] != invalid_value]
        Example: df_cleaned = df_cleaned[df_cleaned['CO(GT)'] != -200] (removes missing data marked as -200).
        Tip: Check for missing values with df.isnull().sum().
    Data Integration
        What: Combine multiple datasets based on a common column.
        Why: Enrich data with additional information (e.g., weather data).
        Code:
            Merge: pd.merge(df1, df2, on='key_column', how='inner')
            Join types: inner, outer, left, right.
        Example: integrated_df = pd.merge(df_cleaned, weather_data, on='Date', how='inner')
        Tip: Ensure matching keys; use synthetic data if no secondary dataset is provided.
    Data Transformation
        What: Modify data for analysis (e.g., normalize, encode, or extract features).
        Why: Prepare data for modeling or visualization.
        Code:
            Normalize: scaler = StandardScaler(); df[['col']] = scaler.fit_transform(df[['col']])
            Date conversion: pd.to_datetime(df['col'], format='format')
            Extract features: df['Year'] = df['Date'].dt.year
        Example: df_cleaned['CO(GT)_scaled'] = scaler.fit_transform(df_cleaned[['CO(GT)']])
        Tip: Use StandardScaler for numerical data; handle categorical data with pd.get_dummies() if needed.
    Error Correcting
        What: Fix outliers or inconsistent data.
        Why: Prevent skewed results in analysis or modeling.
        Code:
            Cap outliers: df['col'].clip(upper=threshold)
            Ensure valid range: df['col'].clip(lower=0)
            Quantile for outliers: `df['planations for each operation’s purpose (e.g., “Cleaning removes invalid data to improve model accuracy”).

    Be ready to tweak code for different columns or datasets.

Quick Cheatsheet
Operation
	
Function/Code
	
Example Usage
Load CSV
	
pd.read_csv('file.csv', sep=';')
	
pd.read_csv('AirQualityUCI.csv', sep=';')
Drop NaN
	
df.dropna()
	
df.dropna()
Filter Invalid
	
df[df['col'] != value]
	
df[df['CO(GT)'] != -200]
Merge Data
	
pd.merge(df1, df2, on='key')
	
pd.merge(df, weather_data, on='Date')
Normalize
	
StandardScaler().fit_transform(df[['col']])
	
scaler.fit_transform(df[['CO(GT)']])
Date Conversion
	
pd.to_datetime(df['col'], format='format')
	
pd.to_datetime(df['Date'], format='%d/%m/%Y')
Cap Outliers
	
df['col'].clip(upper=threshold)
	
df['CO(GT)'].clip(upper=co_threshold)
Train-Test Split
	
train_test_split(X, y, test_size=0.2)
	
train_test_split(X, y, test_size=0.2)
Random Forest
	
RandomForestRegressor(n_estimators=100)
	
model = RandomForestRegressor()
Evaluate Model
	
mean_squared_error(y_test, y_pred)
	
mean_squared_error(y_test, y_pred)
How to Use

    Get the Dataset: Download the Air Quality dataset from UCI Machine Learning Repository (search “Air Quality UCI”). Save it as AirQualityUCI.csv or adjust the file path.
    Run the Code: Use Jupyter Notebook, Google Colab, or a Python IDE. Install libraries (pip install pandas numpy scikit-learn) if needed.
    Check Columns: Verify column names with print(df.columns) and adjust code if necessary (e.g., if CO(GT) is named differently).
    Practice: Modify the code (e.g., predict NO2(GT) instead, or integrate a different synthetic dataset) to build confidence.
    Exam Prep: Use the cheatsheet to recall functions and explain operations during the exam.

If you encounter issues (e.g., file access, column mismatches, or specific operation doubts), let me know, and I can provide further assistance. Good luck with your exam!
