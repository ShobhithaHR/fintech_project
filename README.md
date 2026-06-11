# Bluestock Mutual Fund Analytics Capstone

## Project Overview

Bluestock Mutual Fund Analytics is an end-to-end data analytics project focused on analyzing Indian mutual fund data.

The project includes data extraction, transformation, exploratory data analysis, performance analysis, and interactive dashboard development using Python and Power BI.

The objective is to understand mutual fund trends, investor behavior, fund performance, and category-level growth patterns.

---

# Objectives

- Analyze mutual fund scheme performance
- Study AUM growth trends
- Analyze SIP inflows and investor activity
- Identify top-performing funds
- Build interactive business dashboards
- Create an automated ETL pipeline

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Power BI
- SQL
- GitHub

---

# Project Structure
FINTECH_PROJECT

├── data
│ ├── raw
│ └── processed

├── notebooks
│ ├── EDA Analysis
│ ├── Performance Analytics
│ └── Advanced Analytics

├── scripts
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── run_pipeline.py

├── dashboard
│ └── bluestock_mf_dashboard.pbix

├── outputs
│ └── charts

├── reports

├── requirements.txt

└── README.md


---

# ETL Pipeline

The ETL workflow:


Dataset Files
|
↓
Extract
|
↓
Transform
|
↓
Load
|
↓
Analysis Dashboard


---

# How to Run the Project

## 1. Install dependencies


pip install -r requirements.txt


## 2. Run ETL Pipeline


python scripts/run_pipeline.py


Expected output:


Starting ETL Pipeline...
Data extraction completed.
Data transformation completed.
Data loading completed successfully.
ETL Pipeline completed successfully.


---

# Dataset Description

| Dataset | Description |
|---|---|
| Fund Master | Mutual fund scheme information |
| NAV History | Historical NAV values |
| AUM Data | Assets under management |
| SIP Inflows | Monthly SIP investment trends |
| Category Inflows | Category-wise investment flow |
| Folio Count | Investor account information |
| Performance Data | Fund return analysis |

---

# Dashboard

The Power BI dashboard provides:

- AUM analysis
- Fund performance comparison
- SIP trends
- Category analysis
- Investor insights

Dashboard file:


dashboard/bluestock_mf_dashboard.pbix


---

# Key Findings

- Identified major fund categories contributing to AUM growth
- Compared scheme performance trends
- Analyzed investor investment patterns
- Highlighted top-performing funds

---

# Limitations

- Historical data availability
- Limited external market factors
- No real-time market integration

---

# Future Improvements

- Real-time API integration
- Predictive fund performance models
- Automated dashboard refresh
- Risk-adjusted return analysis

---

## Project Repository

GitHub Link:

https://github.com/ShobhithaHR/fintech_project

# Author

Shobhitha H R

