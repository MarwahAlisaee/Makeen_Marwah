import numpy as np
from sklearn.linear_model import LinearRegression

# Input data
height = np.array([140, 150, 160, 170, 180]).reshape(-1, 1)
shoe_size = np.array([7, 8, 9, 10, 11])

# Create and fit the linear regression model
model = LinearRegression()
model.fit(height, shoe_size)

# Predict shoe size for a given height
height_to_predict = np.array([[165]])  # Example height to predict
predicted_shoe_size = model.predict(height_to_predict)

print("Predicted shoe size:", predicted_shoe_size[0])

