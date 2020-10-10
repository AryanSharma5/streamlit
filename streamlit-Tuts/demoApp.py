import streamlit as st

#st.beta_set_page_config(page_title = 'Demo')


# Title
st.title('Title - Demo app')
# heading
st.header('header - Demo app')
# subheader
st.subheader('subheader - Demo app')
# markdown
st.markdown('markdown - Demo app')
# write
st.write('write - Demo app')
# warning
st.warning('warning - Demo app')
# error
st.error('error - Demo app')
# success
st.success('success - Demo app')
# exception
st.exception('exception - Demo app')
# checkbox
if st.checkbox('select'):
	st.success('selected')

# radio
ans = st.radio('Liked streamlit?', ['Yes', 'No'])
if ans == 'Yes':
	st.success('Hurrah you liked it!!')
elif ans == 'No':
	st.error('Alas!!')

# selectBox
st.selectbox('occupation', ['Other', 'Data Scientist', 'Software Engineer', 'Analyst', 'Doctor'])

# multiselect
selections = st.multiselect('Programming Languages', ['Python', 'C', 'C++', 'Java', 'C#'])
st.write('You selected', len(selections), 'programming languages')

# slider
x = st.slider('x', 0.0, 50.0)
x, 'sqaured is', x**2

# Dataframe
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.dataframe(data = df)

# plot
chart_data = pd.DataFrame(df)

st.line_chart(chart_data)

# Map
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [28.6, 77.18],
    columns=['lat', 'lon'])

st.map(map_data)


# file uploader with progress bar
st.header('Image file uploader')
from PIL import Image
uploadedFile = st.file_uploader('choose an image....', type=['png', 'jpg'])

if st.button('Upload') and uploadedFile:
	
	# progress
	import time
	st.header('progress bar')
	'uploading image...'
	latest_iteration = st.empty()
	bar = st.progress(0)

	for i in range(100):
	  # Update the progress bar with each iteration.
	  #latest_iteration.text(f'Iteration {i+1}')
	  bar.progress(i + 1)
	  time.sleep(0.1)

	'...and now we\'re done!'

	image = Image.open(uploadedFile)
	st.image(image, caption='Uploaded Image', width = 300, use_column_width = False)
