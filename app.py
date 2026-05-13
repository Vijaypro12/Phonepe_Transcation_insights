import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px



st.set_page_config(
    page_title="PhonePe Transaction Insights",
    layout="wide"
)

st.title(" PhonePe Transaction Insights Dashboard")


engine = create_engine(
    "postgresql://postgres:newpassword123@localhost:5432/phonepe_db"
)



st.sidebar.header("Filters")

year_query = "SELECT DISTINCT year FROM aggregated_transcation ORDER BY year"

years = pd.read_sql(year_query, engine)["year"].tolist()

selected_year = st.sidebar.selectbox("Select Year", years)

selected_quarter = st.sidebar.selectbox(
    "Select Quarter",
    [1, 2, 3, 4]
)


query = f"""
SELECT 
    SUM(amount) AS total_amount,
    SUM(count) AS total_transactions
FROM aggregated_transcation
WHERE year = {selected_year}
AND quarter = {selected_quarter};
"""

kpi_df = pd.read_sql(query, engine)

col1, col2 = st.columns(2)

col1.metric(
    "Total Transaction Amount",
    f"₹ {kpi_df['total_amount'][0]:,.0f}"
)

col2.metric(
    "Total Transactions",
    f"{kpi_df['total_transactions'][0]:,.0f}"
)

# -----------------------------------
# TRANSACTION TREND
# -----------------------------------

st.subheader("Transaction Growth Over Time")

query = """
SELECT year, quarter, SUM(amount) AS total_amount
FROM aggregated_transcation
GROUP BY year, quarter
ORDER BY year, quarter;
"""

trend_df = pd.read_sql(query, engine)

trend_df["period"] = (
    trend_df["year"].astype(str)
    + "-Q"
    + trend_df["quarter"].astype(str)
)

fig = px.line(
    trend_df,
    x="period",
    y="total_amount",
    markers=True,
    title="Transaction Trend"
)

st.plotly_chart(fig, use_container_width=True)



st.subheader("Category Analysis")

query = f"""
SELECT category, SUM(amount) AS total
FROM aggregated_transcation
WHERE year = {selected_year}
AND quarter = {selected_quarter}
GROUP BY category
ORDER BY total DESC;
"""

cat_df = pd.read_sql(query, engine)

fig = px.bar(
    cat_df,
    x="category",
    y="total",
    title="Category Wise Transactions"
)

st.plotly_chart(fig, use_container_width=True)



st.subheader("Top States")

query = f"""
SELECT name, SUM(amount) AS total
FROM top_data
WHERE type = 'state'
AND year = {selected_year}
AND quarter = {selected_quarter}
GROUP BY name
ORDER BY total DESC
LIMIT 10;
"""

state_df = pd.read_sql(query, engine)

fig = px.bar(
    state_df,
    x="name",
    y="total",
    title="Top 10 States"
)

st.plotly_chart(fig, use_container_width=True)



st.subheader("Top Districts")

query = f"""
SELECT name AS district, SUM(amount) AS total
FROM top_data
WHERE type = 'district'
AND year = {selected_year}
AND quarter = {selected_quarter}
GROUP BY name
ORDER BY total DESC
LIMIT 10;
"""



district_df = pd.read_sql(query, engine)

fig = px.bar(
    district_df,
    x="district",
    y="total",
    title="Top Districts"
)

st.plotly_chart(fig, use_container_width=True)

