import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Load dataset
df = pd.read_csv("data/loan_data.csv")

# Show basic info
print(f"🔢 Total rows in dataset: {len(df)}")
print(f"🧾 Column names in the dataset:\n{df.columns}")

# Prepare data
X = df.drop(columns=["Default"]) # Features
y = df["Default"]                       # Target label

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("\n=== Model Evaluation ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save the model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/loan_default_model.pkl")
print("\n✅ Model saved as model/loan_model.pkl")
