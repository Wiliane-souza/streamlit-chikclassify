import streamlit as st
import pandas as pd
import pickle

st.title("Diagnóstico de Chikungunya")

with open('model/model.sav', 'rb')as f:
    clf = pickle.load(f)

# CS_SEXO, FEBRE, MIALGIA, CEFALEIA, EXANTEMA, ARTRITE, ARTRALGIA, DOR_RETRO, CLASSI_FIN

with st.form("Diagnostico", clear_on_submit=True):
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
    if sexo == "Masculino":
        sexo = 1
    else: 
        sexo = 2
    
    febre = st.checkbox("Febre")
    if febre:
        febre = 1

    mialgia = st.checkbox("MIALGIA")
    if mialgia:
        mialgia = 1

    cefaleia = st.checkbox("CEFALEIA")
    if cefaleia:
        cefaleia = 1

    exantema = st.checkbox("EXANTEMA")
    if exantema:
        exantema = 1

    artrite = st.checkbox("ARTRITE")
    if artrite:
        artrite = 1

    artralgia = st.checkbox("ARTRALGIA")
    if artralgia:
        artralgia = 1

    dor_retro = st.checkbox("DOR RETROBIRTAL")
    if dor_retro:
        dor_retro = 1

    if st.form_submit_button("Submit"):

        result = clf.predict([[sexo, febre, mialgia, cefaleia, exantema, artrite, artralgia, dor_retro]])[0]

        st.write("submited")

        if result == 1:
            st.write("Provável chikungunya")
        else:
            st.write("Provável não chikungunya")






    # idade = st.number_input("Idade", max_value=150)
    # st.write(idade)
    # data = st.date_input("Data")
    # st.write(data)
