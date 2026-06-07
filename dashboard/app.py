import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mutual Fund Dashboard", layout="wide")

st.title("📊 Mutual Fund Analytics Dashboard")

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    nav = pd.read_csv(r"data/nav_history.csv")
    txn = pd.read_csv(r"data/investor_transactions.csv")
    perf = pd.read_csv(r"data/scheme_performance.csv")
    return nav, txn, perf

nav, txn, perf = load_data()

# ---------- NAV DATA ----------
st.header("NAV History Data")
st.write(nav.head())

st.write("Shape:", nav.shape)

# ---------- TRANSACTIONS ----------
st.header("Investor Transactions")
st.write(txn.head())

st.write("Shape:", txn.shape)

# ---------- PERFORMANCE ----------
st.header("Scheme Performance")
st.write(perf.head())

st.write("Shape:", perf.shape)