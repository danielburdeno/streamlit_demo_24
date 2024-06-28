import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title('Penguin Species Model Prediction')

@st.cache_resource
def load_model(file):
    model_file = open(file, 'rb')
    model = joblib.load(model_file)
    model_file.close()
    return model

penguin_model = load_model('Penguin_Model.pkl')

side = st.sidebar
side.title('Model Inputs')
form1 = side.form(key='Data Input Form')
form1.subheader('Bill Length and Depth')
bill_length = form1.number_input('Enter the bill length (mm)', min_value=0.0)
bill_depth = form1.number_input('Enter the bill depth (mm)', min_value=0.0)
form1.subheader('Flipper Length')
flipper_length = form1.number_input('Enter the flipper length (mm)', min_value=0.0)
form1.subheader('Body Mass')
body_mass = form1.number_input('Enter the body mass (g)', min_value=0.0)
form1.subheader('Sex')
sex = form1.number_input('Enter the sex', min_value=0, max_value=1, step=1, help='0 - Male, 1 - Female')
form1.subheader('Island')
island = form1.selectbox('Select the island', ['Biscoe', 'Dream', 'Torgersen'])
form_button = form1.form_submit_button('Submit Features')

st.header('New Penguin Data')
new_input = [[island, bill_length, bill_depth, flipper_length, body_mass, sex]]
predict_in = pd.DataFrame(new_input, columns=penguin_model.feature_names_in_)
expander_df = st.expander('View your new penguin data')
expander_df.write(predict_in)

predict_button = st.button('Predict Penguin Species')
if predict_button:
    if float(bill_length <=0.0):
        st.write('Please enter a valid bill length')
    else:
        prediction = penguin_model.predict(predict_in)
        st.write(f'The predicted species is {prediction[0]}')