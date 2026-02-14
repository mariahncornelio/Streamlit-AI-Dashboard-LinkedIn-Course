#Build with AI: AI-Powered Dashboards with Streamlit 
#Quick Review: Streamlit Basics for Web Apps

#Import packages
import streamlit as st
from datetime import date, datetime

#Configure page - page, title, layout
st.set_page_config(page_title="Streamlit Basics Review", layout="wide")

#Write title and text - can also do header and subheader
st.title("Streamlit Basics Review")
st.write("Hello World!")

#Gather current date and time
st.write("Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#Create button - that users can press and interact
if st.button("Click me!"):
  st.success("Successfully pressed this button. Yay!")

#Create slider widget
age = st.slider("Your age", 0, 100, 30) # min, max, default
st.write(f"You are {age} years old.")

#Create text input widget - users can enter free form text
name = st.text_input("What is your name?:")
if name:
  st.write(f"Hi, {name}")

#Create checkbox widget
toggle = st.checkbox("Check for a surprise!")
if toggle: # If they do check this checkbox
  st.info("SURPRISEEEEE!!!!1!!!")

#Create multiselect widget
options = st.multiselect("Choose pizza toppings", ["Cheese", "Pepperoni", "Onions"])
st.write("Toppings:", options)

#Create sidebar container - allows users to write in different prompts or work with filters
st.sidebar.title("Sidebar Panel")

#Add selection widget for sidebar
sidebar_option = st.sidebar.selectbox("Select an option:", ["Home", "Settings", "About"])
st.sidebar.write("You chose", sidebar_option) # Add this

#Create three column containers - good to display KPIs
col1, col2, col3 = st.columns(3) # Initiates containers

#Create temperature container
with col1:
  st.metric("Temperature", "72F", "-1.2F") # Can add degree symbol but if not, then F for Fahrenheit works just fine

#Create wind speed container
with col2:
  st.metric("Wind Speed:", "10 mph", "+1.5mph")

#Create humidity container
with col3:
  st.metric("Humidity", "50%", "-5%")

#Create expander container
with st.expander("See more details:"):
  st.write("Here are more details... you can put any Streamlit commands inside expanders.")