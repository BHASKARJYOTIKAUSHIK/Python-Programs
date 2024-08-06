import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Streamlit App')

st.write("This is a simple example of a Streamlit app")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write("Here's a sample dataframe:")
st.write(df)

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

st.write('You selected: ', option)

x = st.slider('Select a value for x', 0, 100, 50)
st.write('The selected value for x is', x)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
