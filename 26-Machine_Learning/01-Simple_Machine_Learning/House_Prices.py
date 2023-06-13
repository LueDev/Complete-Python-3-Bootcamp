'''Here is an example of a simple machine learning program in Python that trains a 
linear regression model to predict the price of a house based on its size:'''

import numpy as np
from sklearn.linear_model import LinearRegression

# Load the training data
X = np.array([[2104], [1600], [2400], [1416], [3000]])
y = np.array([[400], [330], [369], [232], [540]])

# Create the linear regression model
model = LinearRegression()

# Train the model using the training data
model.fit(X, y)

# Predict the price of a house with size 1650 sq. ft.
X_test = np.array([[1650]])
prediction = model.predict(X_test)

print(f"Predicted price of a house with size 1650 sq. ft.: ${prediction[0][0]:.2f}")

'''This code uses the numpy library to load the training data and create the input and output arrays (X and y). 
The input array X represents the sizes of the houses in the training data, and the output array y represents 
their corresponding prices.

The code then creates a LinearRegression model using the LinearRegression class from the sklearn.linear_model 
module. This model represents a linear regression model that can be trained to predict a continuous output 
variable based on one or more input variables.

Next, the code trains the model using the fit method and the training data. The fit method adjusts the model's 
parameters so that it can make predictions that are as close as possible to the actual prices of the houses 
in the training data.

Finally, the code uses the trained model to predict the price of a house with size 1650 sq. ft. It creates 
an input array X_test'''