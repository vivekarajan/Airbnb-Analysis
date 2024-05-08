import pandas as pd
import folium
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd



st.set_page_config(page_title="AirBnb-Analysis", page_icon=":bar_chart:", layout="wide")

st.title("AirBnb-Analysis by VIVEKARAJAN S")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

def load_data():
    # Load data from CSV file
    df = pd.read_csv(r"E:\airbnb project\cleaned_Data.csv")
    return df

df = load_data()

price_range = st.sidebar.slider("Price range", min_value=0, max_value=7000, value=(0, 9))
rating_min = st.sidebar.slider("Minimum rating", min_value=20, max_value=100, value=(20,40))

# Filter data based on user inputs
filtered_df = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1]) & (df['reviews'] >= rating_min[0]) & (df['reviews'] <= rating_min[1])]

#st.write(filtered_df)
# Display map
st.title("Distribution of Airbnb listings to explore Prices, Ratings")
st.map(filtered_df[['latitude', 'longitude']].dropna(), zoom=1)