import streamlit as st
import pandas as pd

# -----------------------------
# Title and Description
# -----------------------------
st.title("📊 Sales Summary Dashboard")
st.subheader("Simple interactive app to filter sales by category")

# -----------------------------
# Create Hardcoded Data
# -----------------------------
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Office"],
    "Sales": [80000, 1500, 3000, 12000, 7000]
}

df = pd.DataFrame(data)

# -----------------------------
# Sidebar Filter (Task 2)
# -----------------------------
st.sidebar.header("🔍 Filter Options")

selected_category = st.sidebar.selectbox(
    "Select Category",
    options=df["Category"].unique()
)

# -----------------------------
# Filter Data
# -----------------------------
filtered_df = df[df["Category"] == selected_category]

# -----------------------------
# Display Filtered Data
# -----------------------------
st.write(f"### Showing data for: {selected_category}")
st.dataframe(filtered_df)


# Line Chart (Task 2)
# -----------------------------
st.write("### Sales Trend")
st.line_chart(filtered_df.set_index("Product")["Sales"])
