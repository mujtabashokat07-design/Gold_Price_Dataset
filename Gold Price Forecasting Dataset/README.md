# Gold Price Forecasting Analysis

This Streamlit application provides an interactive analysis of the Gold Price Forecasting Dataset. It allows users to explore historical gold prices, analyze daily returns, and view technical indicators.

## Features

-   **Interactive Dashboard**: Filter data by date range.
-   **Price History**: Visualize the closing price of gold over time.
-   **Technical Indicators**: View 30-day and 90-day Moving Averages and Bollinger Bands.
-   **Statistical Analysis**:
    -   Descriptive statistics of the dataset.
    -   Distribution of daily returns (Histogram & Boxplot).
    -   Correlation heatmap of numerical features.

## Prerequisites

Ensure you have Python installed. You will need the following libraries:

-   streamlit
-   pandas
-   numpy
-   matplotlib
-   seaborn

You can install the dependencies using pip:

```bash
pip install streamlit pandas numpy matplotlib seaborn
```

## How to Run

1.  Navigate to the project directory:
    ```bash
    cd "e:\my document\working folder\Gold Price Forecasting Dataset"
    ```

2.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3.  The application will open in your default web browser.

## Dataset

The application expects a CSV file named `gold_price_forecasting_dataset.csv` in the same directory. This dataset should contain daily gold price data and pre-calculated technical indicators.
