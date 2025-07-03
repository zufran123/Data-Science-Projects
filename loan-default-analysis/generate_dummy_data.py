import pandas as pd
import numpy as np
import os

# Ensure 'data' folder exists
os.makedirs("data", exist_ok=True)

# Generate 1,000 rows of sample loan data
np.random.seed(42)
data = {
    "id": range(1, 1001),
    "feature1": np.random.normal(50, 15, 1000),  # e.g., income
    "feature2": np.random.randint(0, 2, 1000),   # credit history
    "default": np.random.randint(0, 2, 1000)     # binary target
}

df = pd.DataFrame(data)
df.to_csv("data/loan_data.csv", index=False)

print("✅ Dummy dataset created: data/loan_data.csv with 1000 rows.")
