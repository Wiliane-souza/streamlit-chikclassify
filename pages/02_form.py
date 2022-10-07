import streamlit as st

st.title("DotLab - Workshop")

with st.form("form", clear_on_submit=True):
    nome = st.text_input("Nome")
    st.write(nome)
    idade = st.number_input("Idade", max_value=150)
    st.write(idade)
    data = st.date_input("Data")
    st.write(data)

    if st.form_submit_button("Submit"):
        st.write("submited")