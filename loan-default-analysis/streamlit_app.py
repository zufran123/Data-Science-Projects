import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Loan Default Prediction", layout="wide")
st.title("🏦 Loan Default Risk Prediction App")

# Debug
st.write("✅ App loaded")

# Load data
@st.cache_data
def load_data():
    st.write("📊 Loading data...")
    return pd.read_csv("data/loan_data.csv")

# Load model
@st.cache_resource
def load_model():
    st.write("🧠 Loading model...")
    return joblib.load("model/loan_default_model.pkl")

# Try loading everything
try:
    df = load_data()
    model = load_model()
except Exception as e:
    st.error(f"❌ Error during load: {e}")
    st.stop()

st.success("✅ Model and data loaded successfully!")

# Show data preview
with st.expander("📄 View Dataset"):
    st.dataframe(df.head())

# Input fields
st.header("📥 Enter Applicant Details")
user_input = {}
for col in df.drop(columns=["Default"]).columns:
    dtype = df[col].dtype
    if dtype == 'object':
        user_input[col] = st.selectbox(col, df[col].unique())
    else:
        user_input[col] = st.number_input(col, value=float(df[col].mean()))

# Predict
if st.button("🔍 Predict Loan Default Risk"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    st.markdown(f"### 🔎 Prediction: {'❌ Will Default' if prediction == 1 else '✅ Will Not Default'}")
