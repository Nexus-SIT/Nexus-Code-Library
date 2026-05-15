import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Create the data (simulating Google Analytics)
days = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
visitors = np.array([120, 150, 170, 210, 240, 300, 356])

# 2. Train the AI model
model = LinearRegression()
model.fit(days, visitors)

# 3. Make a prediction for Day 8
predicted_val = model.predict([[8]])
print("Data Prepared. AI is ready to predict!")

plt.figure(figsize=(10,6))

# Plot the real data
plt.scatter(days, visitors, color='blue', label='Actual Visitors (G/A4)')

# Plot the AI's "Pattern Line"
plt.plot(days, model.predict(days), color='red', linestyle='--', label='AI Trend Line')

# Plot the prediction for tomorrow.
plt.scatter([8], predicted_val, color='green', s=200, label='AI Prediction')

plt.title('Website Traffic Analytics & AI Prediction')
plt.xlabel('Day')
plt.ylabel('Number of Visitors')
plt.legend()
plt.grid(True)
plt.show()

print(f"Prediction for tomorrow: {int(predicted_val[0])} visitors")
