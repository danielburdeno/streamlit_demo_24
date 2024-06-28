import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Data Summary')
st.header('Data Overview')
st.image('images/penguins.jpg', use_column_width='always')

@st.cache_data
def load_data(path):
    data = pd.read_csv(path, index_col=0)
    return data

penguins = load_data('data/Clean_Penguins.csv')
st.write(penguins)
st.table(penguins.head())
st.dataframe(penguins)

pen_sp = penguins.drop(columns=['island']).groupby(['species', 'sex']).mean()
st.dataframe(pen_sp)

species = penguins['species'].value_counts()
st.bar_chart(species)

def plot_hist(data, title):
    fig, ax = plt.subplots()
    ax.hist(data, bins='auto', stacked=True)
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    return st.pyplot(fig)

cols = list(penguins.columns)
cols.remove('species')
for col in cols:
    plot_hist(penguins[col], title=f'Distribution of {col}')
