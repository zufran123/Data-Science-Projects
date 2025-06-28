# 🔁 Customer Churn Analysis Project

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/zufran123/customer-churn-analysis.svg?style=social)](https://github.com/zufran123/customer-churn-analysis/stargazers)
[![Forks](https://img.shields.io/github/forks/zufran123/customer-churn-analysis.svg?style=social)](https://github.com/zufran123/customer-churn-analysis/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/zufran123/customer-churn-analysis.svg)](https://github.com/zufran123/customer-churn-analysis/commits/main)

---

This Customer Churn Analysis project is a comprehensive, data-driven solution aimed at understanding and predicting customer attrition within the telecom industry.

Using Python and popular machine learning libraries such as Pandas, NumPy, Scikit-learn, and Matplotlib/Seaborn, the project involves thorough data cleaning, exploratory data analysis (EDA), feature engineering, and the application of multiple classification algorithms (e.g., Logistic Regression, Decision Trees, Random Forest, XGBoost) to build robust churn prediction models.

It identifies the most significant factors contributing to customer churn—such as contract type, service usage, tenure, and billing patterns—and translates these findings into actionable business insights. Through model evaluation techniques like confusion matrix, ROC-AUC, precision, and recall, the project ensures high-performance prediction results.

Additionally, the insights derived from this analysis enable telecom companies to design proactive retention strategies, personalize customer outreach, and optimize service offerings. This project not only showcases the practical application of machine learning in solving real-world business problems but also highlights the value of data science in enhancing customer lifetime value and reducing revenue loss.

---

## 📋 Project Management

To streamline the development process, this project was organized using **GitHub Projects**. A dedicated project board was created to plan and track progress efficiently. All key tasks were managed through clearly defined issues, allowing for systematic tracking of milestones such as data exploration, modeling, evaluation, and documentation. This structured approach ensured both productivity and maintainability throughout the project lifecycle.

---

## 📊 Project Overview

- **Objective:** Predict whether a customer will churn (leave) or stay using historical data.
- **Domain:** Telecommunications
- **Problem Type:** Binary Classification
- **Models Used:** Logistic Regression, Decision Tree, Random Forest

---

## 🧰 Tools & Technologies

- **Language:** Python 3.x
- **Libraries Used:**
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - joblib

---

## 📁 Project Structure

```
customer-churn-analysis/
├── data/                  # Contains churn_data.csv
│   └── churn_data.csv
│
├── models/                # Saved ML model files (.pkl)
│   └── LogisticRegression.pkl
│   └── DecisionTree.pkl
│   └── RandomForest.pkl
│
├── src/                   # Python source code
│   └── churn_analysis.py
│
├── visuals/               # Plots and charts (optional)
│
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── .gitignore
```

---

## 🔍 Key Insights Extracted

- 📉 High churn rates were found in customers with month-to-month contracts.
- 💡 Senior citizens and customers with multiple lines had slightly higher churn probability.
- 📶 Customers without internet service had the lowest churn rate.
- 💳 Electronic check payment method showed the highest churn ratio.

---

## 📊 Visualizations Included

- Countplots of churn vs. contract type, internet service, and payment method
- Heatmap showing correlations between numeric features
- Feature importance (for tree-based models)

---

## 🚀 How to Run the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/zufran123/customer-churn-analysis.git
   cd customer-churn-analysis
   ```

2. **Install Required Libraries:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Data:**

   - Ensure `churn_data.csv` is placed inside the `data/` directory.

4. **Run the Model Script:**

   ```bash
   python src/churn_analysis.py
   ```

5. **Check the `models/` Directory:**

   - Trained model files (`.pkl`) will be saved here.

---

## 📂 Dataset Information

- **Source:** [Kaggle or internal dataset — update if applicable]
- **Features:**
  - `customerID`, `gender`, `SeniorCitizen`, `Partner`, `Dependents`
  - `tenure`, `PhoneService`, `MultipleLines`
  - `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, etc.
  - `Contract`, `PaperlessBilling`, `PaymentMethod`
  - `MonthlyCharges`, `TotalCharges`
  - `Churn` (Target)

---

## 📈 Future Improvements

- Add hyperparameter tuning using GridSearchCV
- Improve data cleaning pipeline and handle class imbalance
- Deploy models via a Flask or Streamlit app
- Integrate interactive dashboards for business stakeholders

---

## 🙌 Acknowledgements

- Thanks to open-source contributors and dataset providers.
- Inspired by real-world telecom customer churn prediction challenges.

---

## 👨‍💻 Author

**Mohd Zufran**  
🔗 [LinkedIn](https://linkedin.com/in/mohdzufran)

---

## 📄 License

This Open Source Software is licensed under the **MIT License**.  
Please give proper credit by including the license and attributing the original author.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[MIT License](LICENSE).
