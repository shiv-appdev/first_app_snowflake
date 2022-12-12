import streamlit


streamlit.title('JK bakers')
streamlit.header('FRUITS AND JUICES ')
streamlit.text('smoothie ')
streamlit.text('apple pie')
streamlit.text('Build your own fruit smoothie')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
pd



#Let us put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.



