'''Here is an example of how you can modify the code above to use a decision tree model to predict 
the price of a house based on its size:
'''

import numpy as np
from sklearn.tree import DecisionTreeRegressor

'''This code imports the numpy library and the DecisionTreeRegressor class from the sklearn.tree module. 
It then loads the training data into two arrays: X and y. The input array X represents the sizes of the 
houses in the training data, and the output array y represents their corresponding prices.'''
# Load the training data
X = np.array([[2104], [1600], [2400], [1416], [3000]])
y = np.array([[400], [330], [369], [232], [540]])

'''This code creates a DecisionTreeRegressor object that represents a decision tree model. A decision 
tree model is a non-linear model that can be used to make predictions based on a series of decisions 
made using the input data.'''
# Create the decision tree model
model = DecisionTreeRegressor()

'''This code trains the decision tree model using the fit method and the training data. The fit method 
adjusts the model's parameters so that it can make predictions that are as close as possible to the 
actual prices of the houses in the training data.'''
# Train the model using the training data
model.fit(X, y)

'''This code uses the trained decision tree model to predict the price of a house with size 1650 sq. ft. 
It creates an input array X_test that contains the size of the house, and passes it to the predict method 
of the model. The predict method returns an array of predictions, and in this case, there is only one 
prediction because there is only one test sample. The prediction is printed to the console with a formatted string.'''
# Predict the price of a house with size 1650 sq. ft.
X_test = np.array([[1650]])
prediction = model.predict(X_test)

print(f"Predicted price of a house with size 1650 sq. ft.: ${prediction[0]:.2f}")

'''This code is similar to the previous example, but it uses a DecisionTreeRegressor model from the 
sklearn.tree module instead of a LinearRegression model. A decision tree model is a non-linear model 
that can be used to make predictions based on a series of decisions made using the input data.

To use a decision tree model, you will need to import the DecisionTreeRegressor class and create a 
DecisionTreeRegressor object. You can then train the model using the fit method and the training data, 
and use the model to make predictions using the predict method and the test data.

'''