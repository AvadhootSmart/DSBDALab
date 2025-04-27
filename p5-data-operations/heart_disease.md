Below is the Python code to perform the specified operations on the Heart Disease dataset using Pandas, NumPy, and Scikit-learn, tailored for a beginner in data science with a development background. I'll use the UCI Heart Disease dataset (available from the UCI Machine Learning Repository), which includes features like age, sex, cholesterol, and a target variable indicating heart disease presence. After the code, I'll provide a notes/cheatsheet summarizing the key concepts and functions for these operations.
Python Code for Heart Disease Dataset Operations
python

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

df_cleaned['patient_id'] = range(1, len(df_cleaned) + 1) # Add patient_id
demo_data = pd.DataFrame({
'patient_id': df_cleaned['patient_id'].iloc[:50],
'weight': np.random.uniform(50, 100, 50), # Random weights
'height': np.random.uniform(150, 190, 50) # Random heights
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

Notes/Cheatsheet for Heart Disease Dataset Operations
Dataset Overview

    Heart Disease Dataset: UCI Heart Disease dataset with 14 attributes, including age, sex, chol (cholesterol), trestbps (blood pressure), target (0 = no disease, 1-4 = disease severity).
    Source: UCI Machine Learning Repository (search “Heart Disease UCI”).
    Format: CSV, often without headers, with missing values as ?.
    Key Columns:
        age: Patient age.
        sex: 1 = male, 0 = female.
        chol: Serum cholesterol (mg/dl).
        target: Heart disease (0 = no, 1+ = yes).
        cp: Chest pain type (1-4).
        ca: Number of major vessels (0-3).
        thal: Thalassemia (3 = normal, 6 = fixed, 7 = reversible).

Key Libraries

    Pandas: Data manipulation (pip install pandas).
    NumPy: Numerical operations (pip install numpy).
    Scikit-learn: Machine learning and preprocessing (pip install scikit-learn).
    Import:
    python

    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score

Operations and Functions

    Data Cleaning
        What: Remove or handle missing values, invalid data, or ensure correct data types.
        Why: Clean data is essential for reliable modeling.
        Code:
            Replace and drop NaN: df.replace('?', np.nan).dropna()
            Convert types: pd.to_numeric(df['col'])
        Example: df_cleaned = df.replace('?', np.nan).dropna()
        Tip: Check missing values with df.isnull().sum(); verify types with df.dtypes.
    Data Integration
        What: Combine datasets using a common key (e.g., patient_id).
        Why: Add new features (e.g., weight, height) for richer analysis.
        Code:
            Merge: pd.merge(df1, df2, on='key', how='inner')
        Example: integrated_df = pd.merge(df_cleaned, demo_data, on='patient_id')
        Tip: Use synthetic data if no secondary dataset is provided; ensure key compatibility.
    Data Transformation
        What: Modify data (e.g., normalize numerical features, encode categorical variables).
        Why: Prepare data for machine learning models.
        Code:
            Normalize: scaler = StandardScaler(); df[['col']] = scaler.fit_transform(df[['col']])
            One-hot encode: pd.get_dummies(df, columns=['col'], drop_first=True)
        Example: df_cleaned[[col + '_scaled' for col in numerical_cols]] = scaler.fit_transform(df_cleaned[numerical_cols])
        Tip: Use drop_first=True in get_dummies to avoid multicollinearity.
    Error Correcting
        What: Fix outliers or invalid values.
        Why: Prevent model bias from extreme or incorrect data.
        Code:
            Cap outliers: df['col'].clip(upper=threshold)
            Filter valid range: df[df['col'] >= value]
            Quantile: df['col'].quantile(0.99)
        Example: df_cleaned['chol'] = df_cleaned['chol'].clip(upper=chol_threshold)
        Tip: Use boxplots or df.describe() to identify outliers.
    Data Model Building
        What: Train a machine learning model to predict the target (heart disease).
        Why: Use data to classify patients (disease vs no disease).
        Code:
            Split data: train_test_split(X, y, test_size=0.2, random_state=42)
            Train classifier: RandomForestClassifier(n_estimators=100).fit(X_train, y_train)
            Evaluate: accuracy_score(y_test, y_pred)
        Example: model = RandomForestClassifier(); model.fit(X_train, y_train)
        Tip: Random Forest is robust for classification; use random_state for reproducibility.

General Tips

    Preview Data: Use df.head(), df.info(), df.describe() to inspect structure and stats.
    Handle Dataset Quirks:
        Missing values: Replace ? with np.nan and drop or impute.
        No headers: Specify column names when loading (names=columns).
        Target variable: Convert to binary (0 vs 1+) for simpler classification.
    Practice: Run in Jupyter Notebook or Google Colab. Adjust column names if dataset differs.
    Exam Focus:
        Explain each operation’s purpose (e.g., “Normalization ensures features are on the same scale”).
        Be ready to adapt code for different features or models (e.g., Logistic Regression).

Quick Cheatsheet
Operation
Function/Code
Example Usage
Load CSV
pd.read_csv('file.csv', names=columns)
pd.read_csv('heart_disease.csv', names=columns)
Drop NaN
df.replace('?', np.nan).dropna()
df.replace('?', np.nan).dropna()
Convert Type
pd.to_numeric(df['col'])
pd.to_numeric(df['ca'])
Merge Data
pd.merge(df1, df2, on='key')
pd.merge(df, demo_data, on='patient_id')
Normalize
StandardScaler().fit_transform(df[['col']])
scaler.fit_transform(df[['chol']])
One-Hot Encode
pd.get_dummies(df, columns=['col'])
pd.get_dummies(df, columns=['cp'])
Cap Outliers
df['col'].clip(upper=threshold)
df['chol'].clip(upper=chol_threshold)
Train-Test Split
train_test_split(X, y, test_size=0.2)
train_test_split(X, y, test_size=0.2)
Random Forest
RandomForestClassifier(n_estimators=100)
model = RandomForestClassifier()
Evaluate Model
accuracy_score(y_test, y_pred)
accuracy_score(y_test, y_pred)
How to Use

    Get the Dataset: Download the Heart Disease dataset from UCI Machine Learning Repository (search “Heart Disease UCI”). Save as heart_disease.csv or adjust the file path. The dataset is often named processed.cleveland.data.
    Run the Code: Use Jupyter Notebook, Google Colab, or a Python IDE. Install libraries (pip install pandas numpy scikit-learn) if needed.
    Check Columns: Verify column names with print(df.columns) and ensure they match the specified columns list. Update if necessary.
    Practice: Modify the code (e.g., predict using different features, try Logistic Regression) to build confidence.
    Exam Prep: Use the cheatsheet to recall functions and explain operations during the exam.

If you encounter issues (e.g., file access, column mismatches, or specific operation doubts), let me know, and I can provide further assistance. Best of luck with your exam!
