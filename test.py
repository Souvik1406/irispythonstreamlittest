#Made By Souvik Roys

import pandas as pd
import streamlit as st
import numpy as np

df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
df

st.line_chart(df)

checkbox = st.sidebar.checkbox("Show map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

if checkbox:
  st.map(map_data)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['a'])

'You selected:', option

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


import time

msg = st.empty()
msg.write('Starting a long computation...')

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(50):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress((i + 1)*2)
  time.sleep(0.05)

msg.write('...and now we\'re done!')
st.balloons()




# Get some data.
data = np.random.randn(10, 2)

# Show the data as a chart.
chart = st.line_chart(data)

# Wait 1 second, so the change is clearer.
time.sleep(1)

# Grab some more data.
data2 = np.random.randn(10, 2)

# Append the new data to the existing chart.
chart.add_rows(data2)
