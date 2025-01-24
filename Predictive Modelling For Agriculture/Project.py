# All required libraries are imported here for you.
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the dataset
crops = pd.read_csv("soil_measures.csv")
X = crops.drop("crop", axis=1)
y = crops["crop"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)
features = ["N", "P", "K", "ph"]
print(X_train)
# # Check the columns in the dataset
# print(crops.columns)
scores = {}
for feature in features:
        logreg = LogisticRegression(multi_class = "multinomial")
        train = X_train[feature].values.reshape(-1,1)
        test = X_test[feature].values.reshape(-1,1)
        logreg.fit(train, y_train)
        y_pred = logreg.predict(test)
        f1 = metrics.f1_score(y_test, y_pred, average = "weighted")
        scores[feature] = f1
max_value = 0
for key,value in scores.items() :
    if (value > max_value) :
        max_value = value
        max_key = key
best_predictive_feature = dict()
best_predictive_feature[max_key] = max_value
print(best_predictive_feature)

    
        