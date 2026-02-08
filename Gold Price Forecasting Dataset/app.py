import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Gold Price Analysis", layout="wide")

# Title
st.title("Gold Price Forecasting Dataset Analysis")
st.markdown("Analyze historical gold prices and technical indicators.")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("gold_price_forecasting_dataset.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar - Date Filter
st.sidebar.header("Filter Data")
min_date = df['date'].min()
max_date = df['date'].max()

start_date = st.sidebar.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

if start_date > end_date:
    st.sidebar.error("Start date must be before end date.")
    filtered_df = df
else:
    filtered_df = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

# Main Content - Dataset Overview
st.header("Dataset Overview")
st.markdown(f"Displaying data from **{start_date}** to **{end_date}**.")
st.dataframe(filtered_df.style.format({"daily_return": "{:.2%}", "volatility_7": "{:.4f}"}), use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Descriptive Statistics")
    st.dataframe(filtered_df.describe())
with col2:
    st.subheader("Data Info")
    st.write(f"Total Rows: {len(filtered_df)}")
    st.write(f"Total Columns: {len(filtered_df.columns)}")
    st.write("Missing Values:")
    st.write(filtered_df.isnull().sum()[filtered_df.isnull().sum() > 0])


# Visualizations
st.header("Visualizations")

# 1. Price History
st.subheader("Price History (Close Price)")
fig_price, ax_price = plt.subplots(figsize=(10, 5))
ax_price.plot(filtered_df['date'], filtered_df['close'], label='Close Price', color='gold')
ax_price.set_title("Gold Close Price Over Time")
ax_price.set_xlabel("Date")
ax_price.set_ylabel("Price")
ax_price.legend()
ax_price.grid(True, alpha=0.3)
st.pyplot(fig_price)

# 2. Technical Indicators (Moved Separately)
st.subheader("Technical Indicators")
st.markdown("Moving Averages and Bollinger Bands")
fig_tech, ax_tech = plt.subplots(figsize=(10, 5))
ax_tech.plot(filtered_df['date'], filtered_df['close'], label='Close Price', color='gray', alpha=0.5)
ax_tech.plot(filtered_df['date'], filtered_df['ma_30'], label='30-Day MA', color='blue', linestyle='--')
ax_tech.plot(filtered_df['date'], filtered_df['ma_90'], label='90-Day MA', color='red', linestyle='--')
ax_tech.fill_between(filtered_df['date'], filtered_df['bb_upper'], filtered_df['bb_lower'], color='orange', alpha=0.1, label='Bollinger Bands')
ax_tech.set_title("Technical Indicators")
ax_tech.set_xlabel("Date")
ax_tech.set_ylabel("Price")
ax_tech.legend()
st.pyplot(fig_tech)


# 3. Daily Returns Distribution
st.subheader("Daily Returns Distribution")
col3, col4 = st.columns(2)

with col3:
    fig_hist, ax_hist = plt.subplots()
    sns.histplot(filtered_df['daily_return'], kde=True, ax=ax_hist, color='green')
    ax_hist.set_title("Histogram of Daily Returns")
    st.pyplot(fig_hist)

with col4:
    fig_box, ax_box = plt.subplots()
    sns.boxplot(x=filtered_df['daily_return'], ax=ax_box, color='lightgreen')
    ax_box.set_title("Boxplot of Daily Returns")
    st.pyplot(fig_box)

# 4. Correlation Heatmap
st.subheader("Correlation Heatmap")
fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
# Select only numeric columns for correlation
numeric_df = filtered_df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=False, cmap='coolwarm', ax=ax_corr)
ax_corr.set_title("Feature Correlation Matrix")
st.pyplot(fig_corr)




