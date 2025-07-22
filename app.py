import streamlit as st

st.title('Semantic Movie Search')
st.text_input('Enter movie description')
if st.button('Search'):
    st.write('Top 3 Matches:')