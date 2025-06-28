import sys
sys.stdout.reconfigure(encoding='utf-8')

try:
    print("\n📊 Dataset Overview:")
except UnicodeEncodeError:
    print("\n[Dataset Overview]:")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.backends.backend_pdf import PdfPages

# Smart path handling
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "dataset", "sales_data.csv")

# Load dataset
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Dataset not found at {data_path}")

df = pd.read_csv(data_path)

# Preprocess Date and Time
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Weekday'] = df['Date'].dt.day_name()
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour  # fixed parsing warning

# Basic Overview
print("\n📊 Dataset Overview:")
print(df.head())
print("\nℹ️ Dataset Info:")
print(df.info())
print("\n🧮 Summary Stats:")
print(df.describe())
print("\n🔍 Null Values:")
print(df.isnull().sum())

# Insights
print("\n💰 Total Revenue: ₹", round(df['Total'].sum(), 2))
print("🧾 Average Invoice Amount: ₹", round(df['Total'].mean(), 2))
print("🏆 Top 3 Product Lines:\n", df["Product line"].value_counts().head(3))

# ----------------- Visualizations -------------------
sns.set(style="whitegrid")

pdf_path = os.path.join(base_dir, "sales_report.pdf")
with PdfPages(pdf_path) as pdf:

    # Product Line Sales
    plt.figure(figsize=(10,6))
    sns.barplot(x='Product line', y='Total', data=df, estimator=sum, errorbar=None)
    plt.title("Total Sales per Product Line")
    plt.xticks(rotation=45)
    plt.tight_layout()
    pdf.savefig()
    plt.show()

    # City-wise Revenue
    plt.figure(figsize=(8,5))
    sns.boxplot(x='City', y='Total', data=df)
    plt.title("Revenue Distribution by City")
    plt.tight_layout()
    pdf.savefig()
    plt.show()

    # Gender Spending
    plt.figure(figsize=(8,5))
    sns.barplot(x='Gender', y='Total', data=df, estimator='mean', errorbar=None)
    plt.title("Average Spending by Gender")
    plt.tight_layout()
    pdf.savefig()
    plt.show()

    # Correlation Heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    pdf.savefig()
    plt.show()

    # Monthly Revenue
    monthly_sales = df.groupby('Month')['Total'].sum()
    plt.figure(figsize=(8,5))
    monthly_sales.plot(kind='bar', color='skyblue')
    plt.title("Monthly Revenue")
    plt.ylabel("Revenue")
    plt.tight_layout()
    pdf.savefig()
    plt.show()

    # Hourly Sales Trend
    hourly_sales = df.groupby('Hour')['Total'].sum()
    plt.figure(figsize=(8,5))
    hourly_sales.plot(kind='line', marker='o', color='green')
    plt.title("Hourly Sales Trend")
    plt.xlabel("Hour")
    plt.ylabel("Revenue")
    plt.grid()
    plt.tight_layout()
    pdf.savefig()
    plt.show()

    # Customer Type by Gender
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x='Customer type', hue='Gender')
    plt.title("Customer Type by Gender")
    plt.tight_layout()
    pdf.savefig()
    plt.show()

    # Payment Method Pie Chart
    plt.figure(figsize=(6,6))
    df['Payment'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Payment Methods")
    plt.ylabel("")
    plt.tight_layout()
    pdf.savefig()
    plt.show()

    # Weekday Sales
    weekday_sales = df.groupby('Weekday')['Total'].sum().reindex(
        ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    )
    plt.figure(figsize=(8,5))
    weekday_sales.plot(kind='bar', color='orange')
    plt.title("Sales by Weekday")
    plt.ylabel("Revenue")
    plt.tight_layout()
    pdf.savefig()
    plt.show()

    # Quantity sold by Product Line
    plt.figure(figsize=(10,6))
    sns.barplot(x='Product line', y='Quantity', data=df, estimator=sum, errorbar=None)
    plt.title("Total Quantity Sold per Product Line")
    plt.xticks(rotation=45)
    plt.tight_layout()
    pdf.savefig()
    plt.show()

print(f"📄 PDF report generated: {pdf_path}")
