import streamlit as st

st.title('Penguin Predictor Demo App')
st.header('This is a header')
st.subheader('This is a subheader')

st.sidebar.title('This is the Sidebar Title')
sidebar = st.sidebar
sidebar.subheader('This is the Sidebar Header')

side_button = sidebar.button('Click me')
if side_button:
    sidebar.write('Button clicked')
else:
    sidebar.write('Button not clicked')
    
st.write('This is a normal text')

col1, col2 = st.columns(2)
col1.write('This is column 1')
col2.write('This is column 2')

st.write('This is a normal text')

col2.write('This is column 2 take 2')

col21, col22, col23 = st.columns([3,2,1])
col21.write('This is column 1 - biggest')
col22.write('This is column 2 - medium')
col23.write('This is column 3 - smallest')

st.markdown('Markdown *syntax* works **here**')

'## This is a markdown header'

st.write('<h2 style="text-align:center"> Text aligned with HTML </h2>', unsafe_allow_html=True)

check = st.checkbox('Check me out')
button_check = st.button('Is box checked?')
if button_check:
    if check:
        st.write('Box is checked')
    else:
        st.write('Box is not checked')
        
animal_options = ['Dog', 'Cat', 'Horse', 'Elephant']
fav_animal = st.radio('What is your favorite animal?', animal_options)
if fav_animal:
    st.write(f'You selected {fav_animal}')
    
fav_animal2 = st.selectbox('What is your favorite animal?', animal_options)
if fav_animal2:
    st.write(f'You selected {fav_animal2}')
    
fav_animal3 = st.multiselect('What are your favorite animals?', animal_options)
if fav_animal3:
    st.write(fav_animal3)
    
in_text = st.text_input('What is your favorite animal?', value="I don't know")
if in_text:
    st.write(f'You typed: {in_text}')
    
in_number = st.number_input('What is your favorite number?', value=42.00, min_value=0.0, max_value=100.0)
if in_number:
    st.write(f'You typed: {in_number}')

slider = st.slider('Select a value', min_value=0, max_value=100, value=50, step=5)
if slider:
    st.write(f'You selected: {slider}')
    
pet_num = st.radio('How many pets do you have?', [0, 1, 2, 3, 4, 5])
if pet_num:
    st.write(f'You have {pet_num} pets')
else:
    st.write('You have no pets')