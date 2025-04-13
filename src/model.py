from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def save_model(model, filename='iris_model.pkl'):
    joblib.dump(model, filename)

def load_model(filename='iris_model.pkl'):
    return joblib.load(filename)