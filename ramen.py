import requests
import streamlit as st
from streamlit_lottie import st_lottie




st.set_page_config(page_title="Ramen Ratings",page_icon=":ramen:",layout="wide")
def load_lottieur(url):
	r=requests.get(url)
	if r.status_code!=200:
		return None
	return r.json()




lottie_coding=load_lottieur("https://assets7.lottiefiles.com/packages/lf20_dzfeml7x.json")

with st.container():
	st.title("This page is used Predict Ramen Ratings")
	st.write("It is used to tell Ramen is delicious or not based on reviews recieved")

	st_lottie(lottie_coding,height=400,key="ramen")

