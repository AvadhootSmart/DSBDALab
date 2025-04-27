import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (example: Heart Disease)
df = pd.read_csv('heart_disease.csv')

# Bar plot: Average cholesterol by sex
sns.barplot(x='sex', y='chol', data=df)
plt.title('Average Cholesterol by Sex')
plt.show()

# Scatter plot: Age vs Cholesterol
plt.scatter(df['age'], df['chol'], c=df['target'], cmap='coolwarm')
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.title('Age vs Cholesterol (Colored by Heart Disease)')
plt.show()

# Heatmap: Correlation matrix
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='Blues')
plt.title('Correlation Matrix')
plt.show()

# For Forest Fire (example): Area burned by month
df_fire = pd.read_csv('forestfires.csv')
sns.boxplot(x='month', y='area', data=df_fire)
plt.title('Area Burned by Month')
plt.show()
