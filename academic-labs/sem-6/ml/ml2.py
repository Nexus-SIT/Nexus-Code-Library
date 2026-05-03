import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# 1. Load the dataset
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseVal'] = data.target  # Add target variable to the dataframe

# 2. Compute the Correlation Matrix
# This helps understand the linear relationship between features
corr_matrix = df.corr()

# 3. Visualize the Correlation Matrix using a Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap (California Housing)')
plt.show()

# 4. Use Pairplot to visualize pairwise relationships
# Note: Since the dataset has many rows, we sample it for faster visualization
sns.pairplot(df.sample(500), diag_kind='kde')
plt.suptitle('Pairwise Relationships between Features', y=1.02)
plt.show()
