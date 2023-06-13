
'''This code imports the pandas library, the DecisionTreeClassifier class from the sklearn.tree module, 
the train_test_split function and the GridSearchCV class from the sklearn.model_selection module, and 
the accuracy_score and confusion_matrix functions from the sklearn.metrics module. These libraries and 
functions will be used to load and preprocess the data, create and train the model, make predictions 
with the model, evaluate the performance of the model, and optimize the model's hyperparameters.'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix


'''This code uses the read_csv function from the pandas library to load the Titanic dataset from a CSV 
file into a Pandas DataFrame. The CSV file should contain the data for the Titanic passengers, including 
their age, sex, passenger class, and survival status.'''
# Load the Titanic dataset
data = pd.read_csv('titanic.csv')

'''This code preprocesses the data by dropping unnecessary columns, dropping rows with missing values, 
and encoding the Sex column as a numerical value. The drop method is used to remove the Name, Ticket, 
and Cabin columns from the DataFrame, and the dropna method is used to remove rows with missing values. 
The map method is used to map the string values in the Sex column to numerical values'''
# Preprocess the data
data = data.drop(['Name', 'Ticket', 'Cabin'], axis=1)
data = data.dropna()
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})


'''This code uses the train_test_split function from the sklearn.model_selection module to split the data 
into training and test sets. The input data is split into two arrays: X and y. The X array contains the input
features of the data, and the y array contains the corresponding output values.

The train_test_split function takes the X and y arrays as input, along with a test_size parameter that 
specifies the proportion of the data that should be allocated to the test set. In this case, the test set 
is set to 20% of the data, and the training set is set to 80% of the data.

The function then randomly shuffles the data and divides it into the training and test sets. It returns 
four arrays: X_train, X_test, y_train, and y_test, which contain the input and output values for the 
training and test sets, respectively.

The training set is used to train the machine learning model, and the test set is used to evaluate the 
performance of the model. Splitting the data into training and test sets helps to prevent overfitting, 
which is when a model performs well on the training data but poorly on new, unseen data.
'''
# Split the data into training and test sets
X = data.drop(['Survived'], axis=1)
y = data['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

'''This code creates a DecisionTreeClassifier object that represents a decision tree model for 
classification tasks. A decision tree model is a non-linear model that can be used to make predictions 
based on a series of decisions made using the input data.'''
# Create the decision tree model
model = DecisionTreeClassifier()

'''This code uses the GridSearchCV class from the sklearn.model_selection module to perform grid search 
to find the best hyperparameters for the decision tree model.

Grid search is an exhaustive search algorithm that tries out all possible combinations of hyperparameter 
values and selects the combination that results in the best performance of the model. It is a commonly 
used method for hyperparameter optimization, especially when the search space is small and the performance 
of the model is sensitive to the hyperparameters.

The GridSearchCV class takes the model, a dictionary of hyperparameter values to try, and the number of 
cross-validation folds as input. It trains and evaluates the model for each combination of hyperparameters 
using cross-validation, and it returns the combination that results in the best performance.

In this case, the grid search algorithm tries out all combinations of the max_depth and min_samples_leaf
hyperparameters. The max_depth hyperparameter determines the maximum depth of the decision tree, and the 
min_samples_leaf hyperparameter determines the minimum number of samples required to be at a leaf node.'''
# Use grid search to find the best hyperparameters for the model
param_grid = {'max_depth': [3, 5, 7, 9], 'min_samples_leaf': [1, 3, 5, 7]}
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

'''This code trains the model using the best hyperparameters found by the grid search algorithm. 
It retrieves the best model using the best_estimator_ attribute of the GridSearchCV object, and it 
trains the model using the fit method and the training data.'''
# Train the model using the best hyperparameters
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)


'''This code uses the predict method of the best_model object to make predictions on the test data. 
The predict method takes the test data as input and returns an array of predicted output values.'''
# Make predictions on the test data
y_pred = best_model.predict(X_test)


'''This code calculates and prints the accuracy and confusion matrix of the model. The accuracy is 
the proportion of correct predictions made by the model, and the confusion matrix is a table that 
shows the number of correct and incorrect predictions made by the model for each class.

The accuracy_score function from the sklearn.metrics module is used to calculate the accuracy of 
the model. It takes the true output values and the predicted output values as input and returns 
the accuracy as a float value between 0 and 1.

The confusion_matrix function from the sklearn.metrics module is used to calculate the confusion 
matrix of the model. It takes the true output values and the predicted output values as input and 
returns the confusion matrix as a 2D array.

The results are printed to the console using the print function and string formatting. The f"..." 
syntax is used to create a formatted string that includes variables. The {variable:.2f} syntax is 
used to include the value of a variable in the string, with a fixed width of 2 decimal places.'''
# Calculate and print the accuracy and confusion matrix of the model
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(f"Confusion matrix:")
print(confusion)
