import streamlit as st

st.title("Pokedex")

if 'pokedex' not in st.session_state:
    st.session_state['pokedex']= {'pikachu':'data'}


st.selectbox('View generated entries',st.session_state['pokedex'].keys())
