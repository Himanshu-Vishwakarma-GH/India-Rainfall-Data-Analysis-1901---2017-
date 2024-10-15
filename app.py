import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Loading the dataset
data = pd.read_csv('dataset.csv')

# Print column names to check
print(data.columns)

# Strip whitespace from column names
data.columns = data.columns.str.strip()

# Convert 'ANNUAL' column to numeric for overall rainfall analysis
data['ANNUAL'] = pd.to_numeric(data['ANNUAL'], errors='coerce')

# Handle missing values for 'ANNUAL'
data.fillna(data['ANNUAL'].mean(), inplace=True)

# Streamlit title
st.title("India Rainfall Data Analysis (1901 - 2017)")

# Sidebar for subdivision selection
subdivision = st.sidebar.selectbox('Select Subdivision', data['SUBDIVISION'].unique())

# Filter data for the selected subdivision
subdivision_data = data[data['SUBDIVISION'] == subdivision]

# Display rainfall statistics
st.subheader(f"Rainfall Statistics For {subdivision}")
st.write(subdivision_data.describe())

# Line chart for annual rainfall trend in the selected subdivision
st.subheader(f"Annual Rainfall Trend In {subdivision}")
fig, ax = plt.subplots()
ax.plot(subdivision_data['YEAR'], subdivision_data['ANNUAL'], label='Annual Rainfall (mm)', marker='o')
ax.set_xlabel('Year')
ax.set_ylabel('Annual Rainfall (mm)')
ax.set_title(f'Annual Rainfall Trend In {subdivision} (1901-2017)')
ax.legend()
st.pyplot(fig)


# Conclusions and Suggestions
st.subheader("Conclusions and Suggestions")

# Analyzing the data trends
if subdivision_data['ANNUAL'].mean() > data['ANNUAL'].mean():
    st.write(f"The average annual rainfall in {subdivision} is above the national average.")
    st.write("This may indicate favorable conditions for agriculture but could also raise concerns about flooding.")
else:
    st.write(f"The average annual rainfall in {subdivision} is below the national average.")
    st.write("This could lead to drought conditions affecting crop yields and water supply.")

# Suggest user actions based on analysis
st.write("### Suggested Actions:")
st.write("- **For farmers**: Consider adjusting planting schedules based on expected rainfall trends.")
st.write("- **For policymakers**: Review water management strategies to address potential drought or flood risks.")
st.write("- **For researchers**: Explore deeper insights into climate patterns and their impact on local ecosystems.")
