import streamlit
streamlit.title('JK bakers')
streamlit.header('FRUITS AND JUICES ')
streamlit.text('smoothie ')
streamlit.text('apple pie')
streamlit.text('Build your own fruit smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Display the table on the page.
streamlit.dataframe('my_fruit_list')



