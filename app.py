import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Median House Price', 0, 500001, 20000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type'
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# 显示radio button用于选择收入等级
income_level = st.sidebar.radio(
    "select income level:",
    ('Low','Medium','High')
)


# filter by population
df = df[df.median_house_value >= price_filter]

# filter by capital
df = df[df.ocean_proximity.isin(location_filter)]

# 基于选择的收入等级进行筛选
if income_level == 'Low(<=2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium(>2.5 & < 4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]


# show on map
st.map(filtered_df)

# Display a subheader for the histogran
st.subheader('median house price')
st.write(df[['city', 'country', 'population']])

# show the plot
st.subheader('Total Population By Country')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)