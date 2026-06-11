% Bluestock Mutual Fund Analytics Capstone
% End-to-End Mutual Fund Data Analytics Project
% Shobhitha H R | 11 June 2026

---

# Problem Statement & Objective

## Problem Statement

Mutual fund data is available across multiple datasets, making it difficult to analyze investment trends, compare fund performance, and understand investor behavior.

## Objectives

- Analyze mutual fund scheme performance
- Study Assets Under Management (AUM) growth
- Analyze SIP investment trends
- Compare mutual fund categories
- Identify top-performing funds
- Build automated ETL pipeline
- Develop interactive Power BI dashboards


---

# Data Sources

The project uses multiple mutual fund datasets:

- Fund Master
- NAV History
- AUM Data
- SIP Inflows
- Category Inflows
- Folio Count
- Scheme Performance
- Investor Transactions

These datasets provide insights into:

- Fund performance
- Investor participation
- Investment trends
- Category growth


---

# Project Architecture
Raw Mutual Fund Data

    ↓

Python ETL Pipeline

    ↓

Clean Processed Data

    ↓

Exploratory Data Analysis

    ↓

Performance Analytics

    ↓

Power BI Dashboard

    ↓

Business Insights



---

# ETL Pipeline Design

## Extract

- Reads mutual fund CSV datasets
- Loads raw information into the pipeline

## Transform

- Removes duplicate records
- Handles missing values
- Standardizes column names
- Performs data cleaning

## Load

- Stores processed datasets
- Prepares data for analytics and visualization


Pipeline Execution:


python scripts/run_pipeline.py



---

# EDA Highlights - AUM & NAV Analysis

## AUM Analysis

Key Findings:

- AUM growth indicates increasing investor participation
- Large fund houses contribute significant market share
- Category-level analysis identifies investment trends

## NAV Analysis

Insights:

- Historical NAV movement was analyzed
- Long-term trends help compare fund performance


---

# EDA Highlights - SIP & Investor Trends

## SIP Analysis

Findings:

- SIP investments show consistent growth
- Monthly trends indicate investor behavior
- Increasing SIP flows show higher mutual fund adoption

## Investor Analytics

Analysis includes:

- Folio trends
- Investor participation
- Investment patterns


---

# Performance Metrics - Fund Analysis

Performance evaluation considered:

- Historical returns
- NAV movement
- AUM size
- Investor participation

Insights:

- Top-performing funds were identified
- Fund performance was compared
- Growth patterns were analyzed


---

# Performance Metrics - Category Analysis

Category analysis focused on:

- Equity Funds
- Debt Funds
- Hybrid Funds

Findings:

- Different categories show different growth patterns
- Investor preferences vary across categories
- Category analysis supports investment decisions


---

# Dashboard Screenshot - Industry Overview

Power BI dashboard provides:

- Industry summary
- AUM trends
- Category distribution
- Market overview


![Industry Overview](Screenshots/Page_1_Industry_Overview.png)


---

# Dashboard Screenshot - Fund Performance

Power BI dashboard provides:

- Fund comparison
- Performance metrics
- Scheme-level insights


![Fund Performance](Screenshots/Page_2_Fund_Performance.png)


---

# Dashboard Screenshot - Investor Analytics

The dashboard analyzes:

- Investor participation
- Folio trends
- Investment behavior


![Investor Analytics](Screenshots/page_3_Investor_Analytics.png)


---

# Dashboard Screenshot - SIP & Market Trends

The dashboard highlights:

- SIP investment trends
- Monthly inflows
- Market movement insights


![SIP Trends](Screenshots/Page_4_SIP&Market_Trends.png)


---

# Key Findings

Major insights from the project:

- AUM growth reflects increasing investor confidence
- SIP investments show long-term participation
- Fund performance varies across categories
- Power BI dashboards improve decision-making
- ETL automation improves data preparation efficiency


---

# Recommendations

Future improvements:

- Real-time financial API integration
- Predictive analytics models
- Risk-adjusted return analysis
- Automated dashboard refresh
- AI-based fund recommendations
- Portfolio optimization


---

# Thank You

## Bluestock Mutual Fund Analytics Capstone

Python | SQL | Power BI | Data Analytics


Prepared By:

Shobhitha H R

11 June 2026