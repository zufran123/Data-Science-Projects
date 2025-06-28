import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def load_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)
    return df

def preprocess_data(df):
    for col in df.select_dtypes(include='object').columns:
        if col != 'customerID':
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
    df.drop('customerID', axis=1, inplace=True)
    return df

def train_models(X_train, y_train):
    models_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models")
    os.makedirs(models_dir, exist_ok=True)  # ✅ Create the models directory if it doesn't exist

    models = {
        'LogisticRegression': LogisticRegression(max_iter=1000),
        'DecisionTree': DecisionTreeClassifier(max_depth=5),
        'RandomForest': RandomForestClassifier(n_estimators=100)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        model_path = os.path.join(models_dir, f"{name}.pkl")
        joblib.dump(model, model_path)
        print(f"{name} trained and saved at {model_path}.")

    return models

from sklearn.exceptions import UndefinedMetricWarning
import warnings

warnings.filterwarnings("ignore", category=UndefinedMetricWarning)

def evaluate_models(models, X_test, y_test):
    for name, model in models.items():
        print(f"\n{name} Evaluation:")
        preds = model.predict(X_test)
        print(classification_report(y_test, preds, zero_division=0))


if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "churn_data.csv")
    if not os.path.exists(data_path):
        print("Dataset not found at", data_path)
        exit()

    df = load_data(data_path)
    df = preprocess_data(df)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    from sklearn.preprocessing import StandardScaler

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y  # Ensures balanced classes in train/test
    )

    # Feature scaling (optional but good for Logistic Regression)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    models = train_models(X_train, y_train)
    evaluate_models(models, X_test, y_test)
