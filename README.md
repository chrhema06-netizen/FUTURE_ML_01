# 📊 Sales Forecasting Project

## 📌 Overview

This project predicts future sales using historical data from a retail store dataset.
It also provides useful business insights like which categories and regions perform the best.

---

## 🎯 Objectives

* Analyze past sales data
* Predict future sales trends
* Identify top-performing categories and regions

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

## 📂 Dataset

The dataset used is the **Superstore dataset**, which includes:

* Order Date
* Sales
* Category
* Region
* Product Name

---

## ⚙️ Project Workflow

### 1️⃣ Data Cleaning

* Removed unnecessary spaces in column names
* Converted "Order Date" into proper datetime format
* Handled missing values

### 2️⃣ Data Processing

* Converted daily data into **monthly sales**
* Created a time-based feature for prediction

### 3️⃣ Model Building

* Used **Linear Regression**
* Trained model on past sales data

### 4️⃣ Forecasting

* Predicted sales for the **next 12 months**

### 5️⃣ Visualization

* Sales Forecast graph
* Category-wise Sales graph
* Region-wise Sales graph

---

## 📈 Output Graphs

### 🔹 Sales Forecast

![Sales Forecast](forecast.png)

### 🔹 Category-wise Sales

![Category Sales](category.png)

### 🔹 Region-wise Sales

![Region Sales](region.png)

---

## 📊 Results & Insights

* Sales trends over time were identified
* Certain categories contribute more to total sales
* Some regions perform better than others

---

## 🚀 How to Run the Project

1. Install required libraries:
   pip install pandas matplotlib scikit-learn

2. Run the code:
   python main.py

---

## 📁 Project Structure

sales-forecasting-project/
│── main.py
│── superstore.csv
│── forecast_output.csv
│── README.md
│── forecast.png
│── category.png
│── region.png

---

## 🔮 Future Improvements

* Use advanced models like ARIMA / Prophet
* Build an interactive dashboard
* Improve prediction accuracy

---

## 👩‍💻 Author

Your Name
Rhema Choppala
