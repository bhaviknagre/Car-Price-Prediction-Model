import streamlit as st
import pandas as pd
import pickle
import locale
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline


with open('Linear Regression Model.pkl', 'rb') as file:
    model = pickle.load(file)

locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')


st.title("Car Price Prediction App")
st.write("Predict the price of a used car based on its features.")


def user_input_features():
    company = st.selectbox('Company', model.named_steps['columntransformer'].transformers_[0][1].categories_[1])
    name = st.selectbox('Car Name', model.named_steps['columntransformer'].transformers_[0][1].categories_[0])
    fuel_type = st.selectbox('Fuel Type', model.named_steps['columntransformer'].transformers_[0][1].categories_[2])
    year = st.slider('Year of Manufacture', min_value=2000, max_value=2023, value=2015)
    km_driven = st.number_input('Kilometers Driven', min_value=0, max_value=300000, value=20000)


    input_data = pd.DataFrame({
        'company': [company],
        'name': [name],
        'fuel_type': [fuel_type],
        'year': [year],
        'kms_driven': [km_driven]
    })
    return input_data


input_data = user_input_features()


st.write("## Input Details")
st.write(input_data)


if st.button("Predict Car Price"):
    prediction = model.predict(input_data)
    formatted_price = locale.currency(prediction[0], symbol=True, grouping=True)
    st.write(f"### Predicted Car Price: {formatted_price} INR")

