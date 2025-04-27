import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for better aesthetics
sns.set_style("whitegrid")

# Load the Heart Disease dataset
# Replace 'heart_disease.csv' with the actual file path
# UCI dataset often has no header, so we specify column names
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
           'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
df = pd.read_csv('heart_disease.csv', names=columns)

# Basic data cleaning for visualization
# Replace '?' with NaN and drop missing values
df = df.replace('?', pd.NA).dropna()
# Convert relevant columns to numeric
df[['age', 'chol', 'trestbps', 'thalach', 'ca', 'thal']] = df[[
    'age', 'chol', 'trestbps', 'thalach', 'ca', 'thal']].apply(pd.to_numeric)
# Simplify target to binary (0 = no disease, 1 = disease)
df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)

# Display first few rows to understand the dataset
print("Dataset Preview:")
print(df.head())
print("\n")

# Plot 1: Histogram - Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, color='blue', kde=True)
plt.title('Age Distribution of Patients')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Plot 2: Box Plot - Cholesterol by Target
plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='chol', data=df, palette='Blues')
plt.title('Cholesterol Levels by Heart Disease Status')
plt.xlabel('Heart Disease (0 = No, 1 = Yes)')
plt.ylabel('Cholesterol (mg/dl)')
plt.tight_layout()
plt.show()

# Plot 3: Scatter Plot - Age vs Cholesterol
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='chol', hue='target',
                size='target', data=df, palette='coolwarm')
plt.title('Age vs Cholesterol by Heart Disease Status')
plt.xlabel('Age')
plt.ylabel('Cholesterol (mg/dl)')
plt.tight_layout()
plt.show()

# Plot 4: Heatmap - Correlation Matrix
plt.figure(figsize=(10, 6))
numerical_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']
corr = df[numerical_cols].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features')
plt.tight_layout()
plt.show()

# Plot 5: Bar Plot - Heart Disease by Chest Pain Type
plt.figure(figsize=(10, 6))
sns.countplot(x='cp', hue='target', data=df, palette='viridis')
plt.title('Heart Disease by Chest Pain Type')
plt.xlabel('Chest Pain Type (0-3)')
plt.ylabel('Count')
plt.legend(title='Heart Disease', labels=['No', 'Yes'])
plt.tight_layout()
plt.show()
