import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load the Heart Disease dataset
# Replace 'heart_disease.csv' with the actual file path
# UCI Heart Disease dataset typically has no header, so we specify column names
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
           'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
df = pd.read_csv('heart_disease.csv', names=columns)

# Display first few rows to understand the dataset
print("Original Dataset Preview:")
print(df.head())
print("\n")

# a. Data Cleaning
# Remove rows with missing values (NaN or '?')
df_cleaned = df.replace('?', np.nan).dropna()
# Ensure correct data types (e.g., convert 'ca' and 'thal' to numeric)
df_cleaned['ca'] = pd.to_numeric(df_cleaned['ca'])
df_cleaned['thal'] = pd.to_numeric(df_cleaned['thal'])
print("Cleaned Data Preview:")
print(df_cleaned.head())
print("\n")

# b. Data Integration
# Create a synthetic dataset for integration (e.g., patient demographics)
# For demo, create a small dataset with matching 'patient_id'
df_cleaned['patient_id'] = range(1, len(df_cleaned) + 1)  # Add patient_id
demo_data = pd.DataFrame({
    'patient_id': df_cleaned['patient_id'].iloc[:50],
    'weight': np.random.uniform(50, 100, 50),  # Random weights
    'height': np.random.uniform(150, 190, 50)  # Random heights
})
# Merge heart disease data with demographic data on 'patient_id'
integrated_df = pd.merge(df_cleaned.iloc[:50], demo_data, on='patient_id', how='inner')
print("Integrated Data Preview:")
print(integrated_df[['patient_id', 'age', 'weight', 'height']].head())
print("\n")

# c. Data Transformation
# Normalize numerical columns (e.g., age, chol, trestbps)
scaler = StandardScaler()
numerical_cols = ['age', 'chol', 'trestbps', 'thalach']
df_cleaned[[col + '_scaled' for col in numerical_cols]] = scaler.fit_transform(df_cleaned[numerical_cols])
# Encode categorical variables (e.g., sex, cp) using one-hot encoding
df_cleaned = pd.get_dummies(df_cleaned, columns=['cp', 'restecg', 'slope', 'thal'], drop_first=True)
print("Transformed Data Preview:")
print(df_cleaned[['age', 'age_scaled', 'chol', 'chol_scaled']].head())
print("\n")

# d. Error Correcting
# Cap outliers (e.g., cholesterol values above 99th percentile)
chol_threshold = df_cleaned['chol'].quantile(0.99)
df_cleaned['chol'] = df_cleaned['chol'].clip(upper=chol_threshold)
# Ensure valid ranges (e.g., age >= 18, chol > 0)
df_cleaned = df_cleaned[df_cleaned['age'] >= 18]
df_cleaned['chol'] = df_cleaned['chol'].clip(lower=0)
print("Error-Corrected Data Preview:")
print(df_cleaned[['age', 'chol']].head())
print("\n")

# e. Data Model Building
# Predict heart disease (target: 0 = no disease, 1+ = disease)
# Simplify target to binary (0 vs 1+)
df_cleaned['target'] = df_cleaned['target'].apply(lambda x: 1 if x > 0 else 0)
# Select features (exclude patient_id and original numerical cols)
features = [col for col in df_cleaned.columns if col not in ['patient_id', 'target', 'age', 'chol', 'trestbps', 'thalach']]
X = df_cleaned[features]
y = df_cleaned['target']
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
print("Sample Predictions:", y_pred[:5])
print("\n")
