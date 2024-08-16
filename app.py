import streamlit as st
import datetime
import requests
#import numpy as np

from geopy.geocoders import Nominatim

st.markdown('''
# NY Taxi Price Generator :taxi:

## Please fullfil the following information:
''')

geolocator = Nominatim(user_agent='streamlit-geocoder')

with st.form('Please fullfil the following information:'):

    d = st.date_input('Date of your pickup', value=None)
    t = st.time_input('Time of your pickup', value=None)

    p_address = st.text_input('Pickup adress:')
    if p_address:
        p_location = geolocator.geocode(p_address)

        if p_location:
            p_lat = p_location.latitude
            p_lon = p_location.longitude
            # p_lat = st.write(f"Latitude: {location.latitude}")
            # p_lon = st.write(f"Longitude: {location.longitude}")
        else:
            st.write('Adress not found')

    d_address = st.text_input('Dropoff adress:')
    if d_address:
        d_location = geolocator.geocode(d_address)

        if d_location:
            d_lat = d_location.latitude
            d_lon = d_location.longitude
            # d_lat = st.write(f"Latitude: {d_location.latitude}")
            # d_lon = st.write(f"Longitude: {d_location.longitude}")
        else:
            st.write('Adress not found')

    passenger = st.slider("Number of passenger", min_value=1, max_value=8, step=1)
    submit_button = st.form_submit_button(label='Submit')

# def manhattan_distance_vectorized(df: pd.DataFrame, start_lat: str, start_lon: str, end_lat: str, end_lon: str) -> dict:
#     earth_radius = 6371
#     p_lat_rad, p_lon_rad = np.radians(df[start_lat]), np.radians(df[start_lon])
#     d_lat_rad, d_lon_rad = np.radians(df[end_lat]), np.radians(df[end_lon])
#     dlon_rad = d_lon_rad - p_lon_rad
#     dlat_rad = d_lat_rad - p_lat_rad
#     manhattan_rad = np.abs(dlon_rad) + np.abs(dlat_rad)
#     manhattan_km = manhattan_rad * earth_radius
#     return manhattan_km


url = 'https://taxifare.lewagon.ai/predict'

dt = str(d)+" "+str(t)

params = {'pickup_datetime': dt,
          'pickup_longitude': p_lon,
          'pickup_latitude': p_lat,
          'dropoff_longitude': d_lon,
          'dropoff_latitude': d_lat,
          'passenger_count': passenger}

result = requests.get(url,params)
y_pred = result.json()
st.write('The cost of your race will be', f"$ {round(y_pred['fare'], 2)}")
