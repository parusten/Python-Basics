import streamlit as st
import pandas as pd
import pickle
import os
from calendar import month_abbr, day_abbr


# Streamlit App
st.set_page_config(layout='centered', page_title="Temperature")
st.title("Predict Temperature")
st.write("This will predict the temperature from the selected data and selected model")


@st.cache_data
def load_model(filepath):
    with open(filepath, 'rb') as file:
        model = pickle.load(file)
        return model


FILEPATH = os.path.realpath(__file__)  # path of the current working file
DIRPATH = os.path.dirname(FILEPATH)
# print(DIRPATH)
# create absolute path from os module
model_file = os.path.join(DIRPATH, 'data.pickle')
# model_file = "./data.pickle"              # provide relative path
print(model_file)
model = load_model(model_file)


col1, col2, col3 = st.columns(3)

with col1:
    d = st.date_input("Select the date:")
    month = d.month
    day = d.day
    day_name = d.isoweekday()
    # returns month as number
    st.write("Month:", month_abbr[month])
    st.write("Date:", day)    # returns gatee
    st.write("Day Name:", day_abbr[day_name-1])  # returns bar of week
    st.write("Day Name:", day_name)  # returns bar of week

    st.markdown("***")

    temp_noaa = st.slider(
        "NOAA predicted Temp:", 30, 120, 45, key=1)
    st.write("Temp by NOAA:", temp_noaa)

with col2:
    temp2 = st.text_input("Two days prior in Fahrenheit:", "75")
    try:
        st.write("The current movie title is", int(temp2))
    except:
        st.error("Invalid temperature")

    st.markdown("***")
    st.markdown("***")
    
    tempAvg = st.text_input("Accurate avg temp:", "60")
    try:
        st.write("The current movie title is", int(tempAvg))
    except:
        st.error("Invalid temperature")

with col3:
    temp1 = st.slider(
        "One days prior temperature in Fahrenheit:", 30.0, 120.0, 45.0)
    st.write("One day prior temp:", temp1)

day_expressed = [1 if x == day_name else 0 for x in range(1, 8)]
values = (month, day, temp2, temp1, tempAvg, temp_noaa, *day_expressed)
columns = ('month', 'day', 'temp_2', 'temp_1', 'average', 'forecast_noaa', 'week_Mon',
           'week_Tues', 'week_Wed', 'week_Thurs', 'week_Fri',  'week_Sat', 'week_Sun')
dict_data = {x: y for x, y in zip(columns, values)}

df = pd.DataFrame(dict_data, index=[0])
dfPreped = df[['month',
               'day',
               'temp_2',
               'temp_1',
               'average',
               'forecast_noaa',
               'week_Fri',
               'week_Mon',
               'week_Sat',
               'week_Sun',
               'week_Thurs',
               'week_Tues',
               'week_Wed']]
st.write(dfPreped)

prediction = model.predict(dfPreped)
st.write(prediction)
