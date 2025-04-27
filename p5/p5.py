import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load dataset (example: Heart Disease)
df = pd.read_csv('heart_disease.csv')  # Replace with actual file path

# a. Data cleaning
# Remove missing values
df_cleaned = df.dropna()
# Replace invalid values (e.g., negative age)
df_cleaned = df_cleaned[df_cleaned['age'] > 0]
print("Cleaned Data:\n", df_cleaned.head())

# b. Data integration
# Example: Merge with another dataset (e.g., patient demographics)
df_demo = pd.read_csv('demographics.csv')  # Hypothetical second dataset
integrated_df = pd.merge(df_cleaned, df_demo, on='patient_id', how='inner')
print("Integrated Data:\n", integrated_df.head())

# c. Data transformation
# Normalize numerical columns (e.g., cholesterol levels)
scaler = StandardScaler()
df_cleaned['chol_scaled'] = scaler.fit_transform(df_cleaned[['chol']])
# Encode categorical variables (e.g., sex)
df_cleaned['sex'] = df_cleaned['sex'].map({'male': 1, 'female': 0})
print("Transformed Data:\n", df_cleaned.head())

# d. Error correcting
# Example: Cap outliers (e.g., cholesterol > 600)
df_cleaned['chol'] = df_cleaned['chol'].clip(upper=600)
print("Error Corrected Data:\n", df_cleaned.head())

# e. Data model building (e.g., predict heart disease)
X = df_cleaned[['age', 'chol_scaled', 'sex']]  # Features
y = df_cleaned['target']  # Target (1 = disease, 0 = no disease)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)
