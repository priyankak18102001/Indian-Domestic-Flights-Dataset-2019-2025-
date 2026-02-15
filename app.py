import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Flights Dashboard", layout="wide")

st.title("Flights Data Dashboard")

# Load data
df = pd.read_csv("flights.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

st.subheader("Dataset Preview")
st.dataframe(df.head())

# ---- KPI Cards ----
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))

if "year" in df.columns:
    col2.metric("Years Covered", df["year"].nunique())
else:
    col2.metric("Columns", len(df.columns))

if "passengers" in df.columns:
    col3.metric("Total Passengers", int(df["passengers"].sum()))
else:
    col3.metric("Total Rows", len(df))

st.write("---")

# 1 Passenger Trend by Year
if "year" in df.columns and "passengers" in df.columns:
    st.subheader("1. Passenger Trend by Year")
    yearly = df.groupby("year")["passengers"].sum()
    st.line_chart(yearly)

    st.write(
        f"Insight: Passenger traffic increased from {yearly.min():,.0f} to {yearly.max():,.0f}, "
        "showing overall growth in air travel demand."
    )

# 2 Monthly Trend
if "month" in df.columns and "passengers" in df.columns:
    st.subheader("2. Passenger Trend by Month")
    monthly = df.groupby("month")["passengers"].sum()
    st.bar_chart(monthly)

    st.write(
        "Insight: Some months consistently show higher passenger counts, "
        "indicating seasonal travel patterns."
    )

# 3 Histogram
if "passengers" in df.columns:
    st.subheader("3. Passenger Distribution")
    fig, ax = plt.subplots()
    ax.hist(df["passengers"], bins=20)
    st.pyplot(fig)

    st.write(
        "Insight: The histogram shows how passenger counts are distributed. "
        "Most values fall in mid-range, while very high counts are less frequent."
    )

# 4 Average passengers per year
if "year" in df.columns and "passengers" in df.columns:
    st.subheader("4. Average Passengers per Year")
    avg_year = df.groupby("year")["passengers"].mean()
    st.line_chart(avg_year)

    st.write(
        "Insight: The average passengers per year show how travel demand "
        "has gradually changed over time."
    )

# 5 Top busiest months
if "month" in df.columns and "passengers" in df.columns:
    st.subheader("5. Top Busiest Months")
    busy = df.groupby("month")["passengers"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(busy)

    st.write(
        f"Insight: The busiest month is {busy.index[0]}, meaning this month "
        "has the highest air travel demand."
    )

# 6 Box plot
if "passengers" in df.columns:
    st.subheader("6. Passenger Spread (Box Plot)")
    fig, ax = plt.subplots()
    df.boxplot(column="passengers", ax=ax)
    st.pyplot(fig)

    st.write(
        "Insight: The box plot shows median passenger values and spread. "
        "Outliers represent unusually high travel periods."
    )

# 7 Cumulative passengers
if "passengers" in df.columns:
    st.subheader("7. Cumulative Passengers")
    df["cumulative"] = df["passengers"].cumsum()
    st.line_chart(df["cumulative"])

    st.write(
        "Insight: The cumulative curve shows continuous growth in total passengers over time."
    )

# 8 Yearly growth
if "year" in df.columns and "passengers" in df.columns:
    st.subheader("8. Yearly Growth Rate")
    growth = df.groupby("year")["passengers"].sum().pct_change()
    st.line_chart(growth)

    st.write(
        "Insight: Growth rate shows years with faster or slower increases in passenger traffic."
    )

# 9 Summary statistics
st.subheader("9. Summary Statistics")
st.dataframe(df.describe())

st.write(
    "Insight: Summary statistics help understand average, minimum, maximum, "
    "and variability in passenger data."
)

# 10 Correlation table
st.subheader("10. Correlation Table")
st.dataframe(df.corr(numeric_only=True))

st.write(
    "Insight: Correlation values indicate relationships between numeric variables in the dataset."
)
