import pandas as pd
import xgboost
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


# load data
data = pd.read_csv('iris.csv', header=None)
dataset = data.values

# split data into X and y
X = dataset[:, 0:4]
y = dataset[:, 4]

# encode string class values as integers
label_encoder = LabelEncoder()
label_encoder = label_encoder.fit(y)
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, label_encoder,
        test_size=test_size, random_state=seed)
# fit model no training data
model = xgboost.XGBClassifier()
model.fit(X_train, y_train)
print(model)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
