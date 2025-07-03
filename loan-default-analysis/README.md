# 🔁 Loan Default Risk Analysis Project

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/zufran123/loan-default-analysis.svg?style=social)](https://github.com/zufran123/loan-default-analysis/stargazers)
[![Forks](https://img.shields.io/github/forks/zufran123/loan-default-analysis.svg?style=social)](https://github.com/zufran123/loan-default-analysis/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/zufran123/loan-default-analysis.svg)](https://github.com/zufran123/loan-default-analysis/commits/main)

---

This Loan Default Risk Analysis project is a complete, data-driven machine learning solution designed to assess and predict the likelihood of a loan applicant defaulting on their loan. It simulates a real-world financial decision-making process by incorporating key personal and financial attributes of borrowers and applying a classification model to evaluate risk. Built using Python and widely adopted data science libraries such as Pandas, NumPy, Scikit-learn, Streamlit, and FPDF, the project covers the full ML lifecycle — from dataset creation and preprocessing to model training, evaluation, and interactive deployment via a web app. The workflow begins with the generation and loading of a synthetic loan applicant dataset, followed by cleaning, feature preparation, and the training of a Random Forest Classifier. This model is chosen for its robustness and ability to handle nonlinear relationships and feature importance analysis. To ensure interpretability and transparency, the model’s predictions are exposed via an interactive Streamlit-based user interface, which allows users to input hypothetical applicant data (e.g., age, annual income, credit score, loan amount, loan term) and receive a real-time risk prediction. Furthermore, the app automatically generates and allows downloading of a PDF report summarizing the user's input and the model's prediction — useful for documentation or stakeholder sharing.

This system simulates a practical credit scoring pipeline that could be used by lending institutions, microfinance organizations, or credit analysts to:

Pre-qualify applicants

Identify high-risk borrowers

Automate parts of the loan screening process

The model performance is evaluated using key metrics such as accuracy, precision, recall, and F1-score, giving a rounded view of how well the classifier distinguishes between defaulters and non-defaulters.

By streamlining both the predictive backend and user-facing interface, this project demonstrates the real-world application of data science and machine learning in financial risk assessment, showcasing the potential for automating decision pipelines while maintaining interpretability and user interaction.

Ultimately, this project not only highlights the power of machine learning in making informed loan decisions but also serves as a portfolio-ready showcase of technical skills in:

Data analysis

Model training and evaluation

PDF reporting

Streamlit app deployment

GitHub documentation and version control.

⚠️ Challenges Faced :
-> Ensuring the model handled imbalanced class distributions effectively, where defaults are typically less frequent than non-defaults.

-> Avoiding overfitting in tree-based models like Random Forest due to a small, synthetic dataset.

-> Generating realistic synthetic data while maintaining variability and meaningful feature relationships.

-> Handling compatibility issues across Python, NumPy, and scikit-learn versions during local testing and packaging.

-> Maintaining modularity across data generation, model training, reporting, and UI components.

⚖️ Data Imbalance Considerations
-> In real-world financial data, default cases are often underrepresented. To simulate this behavior:

-> The dataset was synthetically generated with a 75:25 split between non-defaulters and defaulters.

-> This helped mimic practical class imbalance and test model generalizability on minority classes.

Note: In future versions, advanced techniques such as SMOTE (Synthetic Minority Oversampling) or cost-sensitive learning could be introduced.

🚀 Future Improvements
-> Integrate SHAP or LIME for model interpretability and feature attribution.

-> Add a live database backend (e.g., SQLite, Firebase, or PostgreSQL) to log all predictions.

-> Incorporate email integration to send PDF reports directly to applicants.

-> Add user authentication for secure multi-user access.

-> Expand model training with hyperparameter tuning using GridSearchCV or Optuna.

-> Add Streamlit Cloud multi-page structure (sidebar navigation).

☁️ Streamlit Deployment Experience
The complete app was deployed on Streamlit Cloud, allowing for real-time interaction with the model through a modern, browser-accessible interface.

Deployment involved:

-> Structuring the codebase for cloud readiness (requirements.txt, fixed paths)

-> Testing compatibility across Python versions and external libraries

-> Streamlining model size, folder structure, and app performance for smooth hosting.

---

## 📋 Project Management

This project was developed with a structured approach involving:

- Python scripts for modularization
- Streamlit for real-time prediction interface
- GitHub for source control and collaboration
- PDF reports to capture individual predictions

---

## 📊 Project Overview

- **Objective:** Predict loan default risk from applicant data
- **Domain:** Finance / Lending
- **Problem Type:** Binary Classification
- **Target Variable:** `Default` (0 = No Default, 1 = Default)
- **Model Used:** Random Forest Classifier

---

## 🧰 Tools & Technologies

- **Language:** Python 3.11+
- **Libraries Used:**
  - pandas
  - numpy
  - scikit-learn
  - streamlit
  - fpdf
  - joblib

---

---

## 📁 Project Structure

```

loan-default-analysis/
├── app/
│ └── streamlit_app.py # Streamlit UI
├── data/
│ └── loan_data.csv # Input dataset
├── model/
│ └── loan_default_model.pkl # Trained model
├── reports/
│ └── loan_risk_report_*.pdf # Auto-generated PDF reports
├── visuals/
│ └── *.png # Plots (optional)
├── main.py # Model training script
├── generate_dummy_data.py # Script to generate synthetic data
├── generate_report.py # PDF report generator
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore
```


---

## 🔍 Key Features

- 📊 Synthetic dataset of 500 loan applicants
- ✅ Random Forest classifier for robust binary classification
- 📄 Automatic PDF report generation using FPDF
- 🧠 Real-time prediction through a responsive Streamlit UI
- 💾 Modularized codebase for flexibility and maintenance

---

## 📈 Visualizations Included

- Feature importance (from the model)
- Correlation heatmaps
- Input value analysis (through Streamlit)

---

## 🚀 How to Run the Project

### 1. Clone the Repository:

```bash
git clone https://github.com/zufran123/loan-default-analysis.git
cd loan-default-analysis
```
### 2. Create Virtual Environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate # Windows
```
### 3. Install Dependencies:

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```
### 4. Train the Model:

```bash
python main.py
```
### 5. Run the App:

```bash
streamlit run app/streamlit_app.py
```

---

## 📂 Dataset Information

- **Format:** CSV
- **Synthetic Fields Used:**
  - `Age`, `AnnualIncome`, `LoanAmount`
  - `CreditScore`, `LoanTerm`
  - `Default` (0 = No, 1 = Yes)

> Dataset is synthetically generated for demonstration purposes.

---

## 📈 Future Improvements

- Add model explainability (SHAP/LIME)
- Expand dataset with real-world features
- Add authentication to the Streamlit app
- Auto-email PDF reports to users

---

## 🙌 Acknowledgements

- Built for academic and demonstration purposes
- Inspired by financial loan risk modeling used in lending platforms and fintech

---

##  Live Demo

Explore the fully interactive Streamlit application here:

👉 [![View on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://zufran123-loan-default-analysis.streamlit.app) 

---

## 👨‍💻 Author

**Mohd Zufran**  
 [![LinkedIn: mohdzufran](https://img.shields.io/badge/LinkedIn-mohdzufran-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/mohdzufran)

---

## 📄 License

This Open Source Software is licensed under the **MIT License**.  
Please give proper credit by including the license and attributing the original author.

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
