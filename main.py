#!/usr/bin/env python 
import langchain_helper as lch
import streamlit as st


st.title("Pet Name Generator")

user_animal_type = st.sidebar.selectbox('What is your name?', ('Cat', 'Dog', 'Parrot', 'Hamster', 'Guinea Pig'))
user_animal_color = st.sidebar.text_area(label= 'What color if your pet?', max_chars=10)


if user_animal_color:
    response = lch.generate_petname(user_animal_type, user_animal_color)
    st.text(response['pet_name'])