import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('🫐 Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Scrambled Eggs')
streamlit.text('🥑 Avocado Toast')

streamlit.header('Build Your Own Smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Added pick list so fruits can be choosen
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Display the table
streamlit.dataframe(my_fruit_list)
