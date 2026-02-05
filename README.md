# 📊 E-Commerce Sales Data Pipeline & Analysis

## 📖 Project Overview

This project simulates a real-world **data auditing and analytics task** for a retail company with a faulty sales data entry system. Due to inconsistent and inaccurate records, management requires a clean and reliable analysis of sales performance, profitability, and customer behavior.

The project builds a complete **data analytics pipeline** using Python — starting from raw CSV files and ending with business insights and visual dashboards.

---

## 🎯 Objectives

* Clean and standardize messy business data
* Merge multiple datasets into a unified analytical model
* Detect and validate revenue calculation errors
* Perform exploratory data analysis (EDA)
* Visualize key business metrics in a mini dashboard
* Extract actionable insights about sales and customers

---

## 📂 Input Datasets

The analysis is based on three CSV files:

| File                       | Description                                             |
| -------------------------- | ------------------------------------------------------- |
| **customers.csv**          | Customer details such as region and demographic data    |
| **products.csv**           | Product information including category and price        |
| **sales_transactions.csv** | Sales records with quantity, discount, and total amount |

---

## 🛠 Technologies Used

* **Python**
* **Pandas** – Data manipulation & cleaning
* **NumPy** – Numerical processing
* **Matplotlib** – Plotting
* **Seaborn** – Statistical data visualization

---

## 🧹 Phase 1: Data Cleaning

The raw datasets contained multiple issues that were addressed:

* Corrected incorrect **data types**
* Converted and standardized **date formats**
* Cleaned numerical values (missing data, invalid entries, inconsistent discounts)
* Standardized string data (regions, categories, duplicates)

---

## 🔗 Phase 2: Data Modeling

All datasets were merged into a single analytical dataset:

```
sales_transactions + customers + products
```

This allows cross-analysis between:

* Customers
* Products
* Transactions

---

## 🧮 Phase 3: Feature Engineering

A new metric was created to validate data accuracy:

```
Calculated_Revenue = Quantity × Unit Price × (1 − Discount)
```

This value was compared with the original **Total_Amount** column to identify potential data entry errors.

---

## 📊 Exploratory Analysis & Visualization

A mini dashboard was built using **Seaborn**, containing:

| Visualization | Purpose                                             |
| ------------- | --------------------------------------------------- |
| 📌 Bar Chart  | Total Revenue by Region                             |
| 📦 Box Plot   | Revenue distribution by Product Category            |
| 🔥 Heatmap    | Correlation between Quantity, Discount, and Revenue |
| 📈 Line Plot  | Monthly Sales Trends over the last year             |

---

## 📈 Key Insights (Examples)

* Certain regions generate significantly higher revenue
* Discounts have a strong influence on profitability
* Some product categories show wide revenue variability
* Sales exhibit seasonal monthly trends

---

## 🧠 Skills Demonstrated

* Data Cleaning & Preprocessing
* Data Modeling & Merging
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Business Data Visualization
* End-to-End Data Analytics Pipeline Design

---

## ▶ How to Run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/ecommerce_sales_analysis.ipynb
```

---

## ⏳ Timeline

* Start Date: **31/01/2026**
* Deadline: **10/02/2026**

---

## 👨‍💻 Project Context

This project was completed as part of a **Data Analytics Libraries using Python** assignment, focusing on transforming raw business data into meaningful insights for decision-making.

---

## 📌 Final Note

This project demonstrates how real-world business data can be cleaned, validated, modeled, and visualized to support strategic and operational decisions.

