import pandas as pd
import streamlit as st

# Set the page layout to wide
st.set_page_config(layout="wide", page_title="PhotoFinish.Live Trueskill Ratings")



# Load the dataset
data = pd.read_csv("trueskill_table.csv")

# App title
st.title("PhotoFinish.Live Trueskill Ratings: Season 25 Juveniles (week 2)")

# Search functionality
search_query = st.text_input("Search by Horse Name:")
if search_query:
    data = data[data["horse_name"].str.contains(search_query, case=False, na=False)]

# Filter functionality
columns_to_filter = ["grade", "archetype"]
filters = {}
for column in columns_to_filter:
    unique_values = sorted(data[column].dropna().unique())
    filters[column] = st.multiselect(f"Filter by {column}", options=unique_values)

# Apply filters
for column, selected_values in filters.items():
    if selected_values:
        data = data[data[column].isin(selected_values)]

# Paginate data
rows_per_page = 50
total_rows = len(data)
page = st.number_input(
    "Page Number", min_value=1, max_value=(total_rows // rows_per_page) + 1, step=1
)
start_idx = (page - 1) * rows_per_page
end_idx = start_idx + rows_per_page

# Display the data without the index
st.write(f"Showing rows {start_idx + 1} to {min(end_idx, total_rows)} of {total_rows}")
st.dataframe(data.iloc[start_idx:end_idx].reset_index(drop=True), use_container_width=True)
