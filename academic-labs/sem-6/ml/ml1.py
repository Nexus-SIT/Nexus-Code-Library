import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# Load the dataset
df = pd.read_csv('california_housing.csv')

# 1. Histograms for all numerical features
df.hist(figsize=(12, 10), bins=30, edgecolor='black')
plt.suptitle('Histograms: Feature Distribution Analysis', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# 2. Box plots to identify outliers
plt.figure(figsize=(15, 8))
sns.boxplot(data=df, orient="h", palette="Set2")
plt.title('Box Plots: Outlier Identification', fontsize=16)
plt.show()

# Brief Distribution & Outlier Analysis
print("Quick Stats for Outlier Detection:")
print(df.describe().loc[['min', 'max', 'mean']])
