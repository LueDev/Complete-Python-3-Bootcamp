'''This code uses the RandomForestClassifier class from the sklearn.ensemble 
module to create a random forest classifier. It then trains the classifier on a 
small dataset using the fit method and makes predictions on a separate test dataset 
using the predict method. Finally, it calculates the accuracy of the predictions 
using the accuracy_score function from the sklearn.metrics module.

When run, this code will output the accuracy of the predictions made by the random 
forest classifier. This is a very simple example of a machine learning model in Python, 
but it should give you an idea of the basic steps involved in creating and evaluating 
a machine learning model.'''

import sklearn
from sklearn.ensemble import RandomForestClassifier

# Load the training data
X_train = [[0, 0], [1, 1]]
y_train = [0, 1]

# Load the test data
X_test = [[0, 1], [1, 0]]
y_test = [1, 0]

# Create a random forest classifier
classifier = RandomForestClassifier()

# Train the classifier on the training data
classifier.fit(X_train, y_train)

# Make predictions on the test data
predictions = classifier.predict(X_test)

# Calculate the accuracy of the predictions
accuracy = sklearn.metrics.accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.2f}")
