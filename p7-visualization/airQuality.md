Below is the Python code to visualize the Air Quality dataset using Matplotlib and Seaborn libraries, tailored for a beginner in data science with a development background. I'll use the UCI Air Quality dataset (available from the UCI Machine Learning Repository), which contains measurements like CO, NO2, and temperature. The visualizations will include various plot types to cover common analysis needs, aligning with the assignment's requirements for visualizing the Air Quality dataset. After the code, I'll provide a viva cheatsheet summarizing key concepts and functions for your exam.
Python Code for Visualizing Air Quality Dataset
python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for better aesthetics

sns.set_style("whitegrid")

# Load the Air Quality dataset

# Replace 'AirQualityUCI.csv' with the actual file path

# Note: UCI dataset uses ; separator and , for decimals

df = pd.read_csv('AirQualityUCI.csv', sep=';', decimal=',')

# Basic data cleaning for visualization

# Remove rows with invalid values (e.g., CO(GT) = -200)

df = df[df['CO(GT)'] != -200]

# Convert Date to datetime

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Display first few rows to understand the dataset

print("Dataset Preview:")
print(df.head())
print("\n")

# Plot 1: Line Plot - CO(GT) over Time

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['CO(GT)'], color='blue', label='CO(GT)')
plt.title('CO Concentration Over Time')
plt.xlabel('Date')
plt.ylabel('CO(GT) (mg/m³)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Box Plot - CO(GT) by Month

df['Month'] = df['Date'].dt.month
plt.figure(figsize=(10, 6))
sns.boxplot(x='Month', y='CO(GT)', data=df, palette='Blues')
plt.title('CO Concentration Distribution by Month')
plt.xlabel('Month')
plt.ylabel('CO(GT) (mg/m³)')
plt.tight_layout()
plt.show()

# Plot 3: Scatter Plot - CO(GT) vs NO2(GT)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='NO2(GT)', y='CO(GT)', data=df, hue='T', size='T', palette='coolwarm')
plt.title('CO vs NO2 Concentration (Colored by Temperature)')
plt.xlabel('NO2(GT) (µg/m³)')
plt.ylabel('CO(GT) (mg/m³)')
plt.tight_layout()
plt.show()

# Plot 4: Heatmap - Correlation Matrix

plt.figure(figsize=(10, 6))

# Select numerical columns for correlation

numerical_cols = ['CO(GT)', 'NO2(GT)', 'NOx(GT)', 'T', 'RH', 'AH']
corr = df[numerical_cols].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f')
plt.title('Correlation Matrix of Air Quality Features')
plt.tight_layout()
plt.show()

# Plot 5: Bar Plot - Average CO(GT) by Hour

df['Hour'] = pd.to_datetime(df['Time'], format='%H.%M.%S').dt.hour
plt.figure(figsize=(10, 6))
sns.barplot(x='Hour', y='CO(GT)', data=df, palette='viridis')
plt.title('Average CO Concentration by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Average CO(GT) (mg/m³)')
plt.tight_layout()
plt.show()

Viva Cheatsheet for Visualizing Air Quality Dataset
Dataset Overview

    Air Quality Dataset: UCI dataset with columns like Date, Time, CO(GT) (carbon monoxide), NO2(GT) (nitrogen dioxide), T (temperature), RH (relative humidity), AH (absolute humidity).
    Source: UCI Machine Learning Repository (search “Air Quality UCI”).
    Format: CSV with ; separator, , for decimals, and missing values as -200.
    Key Columns:
        CO(GT): CO concentration (mg/m³).
        NO2(GT): NO2 concentration (µg/m³).
        T: Temperature (°C).
        Date, Time: Temporal data.

Key Libraries

    Matplotlib: Core plotting library for customizable visualizations (pip install matplotlib).
    Seaborn: High-level library built on Matplotlib for statistical plots (pip install seaborn).
    Pandas: Data manipulation for preparing data (pip install pandas).
    Imports:
    python

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

Visualization Types and Functions

    Line Plot (Matplotlib)
        What: Shows trends over time (e.g., CO concentration over dates).
        Why: Identify temporal patterns or fluctuations.
        Code:
            plt.plot(x, y, label='label')
            Customize: plt.title(), plt.xlabel(), plt.legend(), plt.xticks(rotation=45)
        Example: plt.plot(df['Date'], df['CO(GT)'], label='CO(GT)')
        Viva Answer: “Line plots are used to visualize trends, like how CO levels change over time, helping identify seasonal or daily patterns.”
    Box Plot (Seaborn)
        What: Displays distribution (median, quartiles, outliers) of a variable across categories (e.g., CO by month).
        Why: Understand variability and outliers in data.
        Code:
            sns.boxplot(x='category', y='value', data=df)
        Example: sns.boxplot(x='Month', y='CO(GT)', data=df)
        Viva Answer: “Box plots show the spread and outliers of CO levels per month, useful for comparing seasonal differences.”
    Scatter Plot (Seaborn)
        What: Shows relationship between two continuous variables (e.g., CO vs NO2).
        Why: Identify correlations or clusters, enhanced with color/size for additional variables.
        Code:
            sns.scatterplot(x='col1', y='col2', data=df, hue='col3', size='col3')
        Example: sns.scatterplot(x='NO2(GT)', y='CO(GT)', data=df, hue='T')
        Viva Answer: “Scatter plots reveal relationships between pollutants, with color indicating temperature to show environmental influences.”
    Heatmap (Seaborn)
        What: Visualizes correlation matrix of numerical features.
        Why: Identify strong/weak relationships between variables.
        Code:
            corr = df[cols].corr()
            sns.heatmap(corr, annot=True, cmap='Blues')
        Example: sns.heatmap(df[numerical_cols].corr(), annot=True)
        Viva Answer: “Heatmaps show correlations, helping identify which pollutants (e.g., CO and NO2) are strongly related.”
    Bar Plot (Seaborn)
        What: Shows aggregated values (e.g., average CO by hour).
        Why: Compare categorical data summaries.
        Code:
            sns.barplot(x='category', y='value', data=df)
        Example: sns.barplot(x='Hour', y='CO(GT)', data=df)
        Viva Answer: “Bar plots display average CO levels per hour, useful for identifying peak pollution times.”

General Tips

    Data Preparation:
        Handle missing values: Filter out -200 (e.g., df[df['CO(GT)'] != -200]).
        Convert dates: pd.to_datetime(df['Date'], format='%d/%m/%Y').
        Extract features: df['Month'] = df['Date'].dt.month.
    Plot Customization:
        Size: plt.figure(figsize=(10, 6))
        Labels: plt.title(), plt.xlabel(), plt.ylabel()
        Style: sns.set_style('whitegrid')
        Save: plt.savefig('plot.png')
    Debugging:
        Missing columns: Check df.columns.
        Date errors: Verify format in pd.to_datetime.
        Plot clutter: Use plt.tight_layout() or adjust figsize.
    Practice: Modify plots (e.g., plot NO2(GT) over time, use different colors).
    Exam Focus:
        Explain why each plot type is used (e.g., “Line plots for trends, heatmaps for correlations”).
        Be ready to describe code or interpret a given plot.

Quick Cheatsheet
Plot Type
Function/Code
Example Usage
Line Plot
plt.plot(x, y, label='label')
plt.plot(df['Date'], df['CO(GT)'])
Box Plot
sns.boxplot(x='cat', y='val', data=df)
sns.boxplot(x='Month', y='CO(GT)', data=df)
Scatter Plot
sns.scatterplot(x='col1', y='col2', hue='col3')
sns.scatterplot(x='NO2(GT)', y='CO(GT)', hue='T')
Heatmap
sns.heatmap(corr, annot=True)
sns.heatmap(df[numerical_cols].corr())
Bar Plot
sns.barplot(x='cat', y='val', data=df)
sns.barplot(x='Hour', y='CO(GT)', data=df)
Set Figure Size
plt.figure(figsize=(width, height))
plt.figure(figsize=(10, 6))
Save Plot
plt.savefig('file.png')
plt.savefig('co_plot.png')
Tight Layout
plt.tight_layout()
plt.tight_layout()
How to Use

    Get the Dataset: Download the Air Quality dataset from UCI Machine Learning Repository (search “Air Quality UCI”). Save as AirQualityUCI.csv or adjust the file path.
    Run the Code: Use Jupyter Notebook, Google Colab, or a Python IDE. Install libraries (pip install pandas matplotlib seaborn) if needed.
    Check Columns: Verify column names with print(df.columns) (e.g., CO(GT), NO2(GT), T). Update code if names differ.
    Practice: Modify plots (e.g., plot NOx(GT) vs RH, use different palettes) to build confidence.
    Exam Prep: Use the cheatsheet to recall functions and explain plot purposes. Be ready to interpret visualizations or write plotting code.

If you encounter issues (e.g., file access, column mismatches, or plot customization), let me know, and I can provide further assistance. Good luck with your exam!
