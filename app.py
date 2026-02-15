import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Flights Dashboard", layout="wide")
st.title("Flights Data Dashboard")

# Load data
df = pd.read_csv("flights.csv")
df.columns = df.columns.str.strip().str.lower()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.write("Columns detected:", df.columns)

# KPI
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))

if "year" in df.columns:
    col2.metric("Years Covered", df["year"].nunique())

if "passengers" in df.columns:
    col3.metric("Total Passengers", int(df["passengers"].sum()))

st.write("---")

# 1 Passenger Trend by Year
if {"year","passengers"}.issubset(df.columns):
    st.subheader("1. Passenger Trend by Year")
    yearly = df.groupby("year")["passengers"].sum()
    st.line_chart(yearly)

# 2 Monthly Trend
if {"month","passengers"}.issubset(df.columns):
    st.subheader("2. Passenger Trend by Month")
    monthly = df.groupby("month")["passengers"].sum()
    st.bar_chart(monthly)

# 3 Histogram
if "passengers" in df.columns:
    st.subheader("3. Passenger Distribution")
    fig, ax = plt.subplots()
    ax.hist(df["passengers"], bins=20)
    st.pyplot(fig)

# 4 Average passengers per year
if {"year","passengers"}.issubset(df.columns):
    st.subheader("4. Average Passengers per Year")
    avg_year = df.groupby("year")["passengers"].mean()
    st.line_chart(avg_year)

# 5 Top busiest months
if {"month","passengers"}.issubset(df.columns):
    st.subheader("5. Busiest Months")
    busy = df.groupby("month")["passengers"].sum().sort_values(ascending=False)
    st.bar_chart(busy)

# 6 Box plot
if "passengers" in df.columns:
    st.subheader("6. Passenger Spread")
    fig, ax = plt.subplots()
    df.boxplot(column="passengers", ax=ax)
    st.pyplot(fig)

# 7 Cumulative passengers
if "passengers" in df.columns:
    st.subheader("7. Cumulative Passengers")
    df["cumulative"] = df["passengers"].cumsum()
    st.line_chart(df["cumulative"])

# 8 Yearly growth
if {"year","passengers"}.issubset(df.columns):
    st.subheader("8. Yearly Growth Rate")
    growth = df.groupby("year")["passengers"].sum().pct_change()
    st.line_chart(growth)

# 9 Summary statistics
st.subheader("9. Summary Statistics")
st.dataframe(df.describe())

# 10 Correlation table
st.subheader("10. Correlation Table")
st.dataframe(df.corr(numeric_only=True))
