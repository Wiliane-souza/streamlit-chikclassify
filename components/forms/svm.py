# [
#     'CS_GESTANT', #  1-3 (trimestre), 4-idade gestacional ignorado, 5- Não gestante, 6- Não se aplica, 9-ignorado
#     'FEBRE', # 1 ou 2
#     'NAUSEA',  # 1 ou 2
#     'CONJUNTVIT', # 1 ou 2
#     'ARTRALGIA', # 1 ou 2
#     'PETEQUIA_N', # 1 ou 2
#     'LEUCOPENIA', # 1 ou 2
#     'DIABETES', # 1 ou 2
#     'HEPATOPAT', #
#     'HIPERTENSA', #
# ]

import pickle
import pandas as pd

with open('models/svm.sav', 'rb')as f:
    clf = pickle.load(f)

def svm_form(st):

    st.write("<h5>Teste</h5>", unsafe_allow_html=True)
    
    with st.form("Support Vector Machine", clear_on_submit=True):
        st.write("<p>Informações do paciente</p>", unsafe_allow_html=True)
        st.write("<hr style='margin: 0'>", unsafe_allow_html=True)

        idade_gestacional = st.selectbox("Idade Gestacional", [
            "Ignorado",
            "1º Trimestre",
            "2º Trimestre",
            "3º Trimestre",
            "Idade gestacional ignorada",
            "Não gestante",
            "Não se aplica (Crianças)"
        ])
        if idade_gestacional == "1º Trimestre":
            idade_gestacional = 1
        elif idade_gestacional == "2º Trimestre":
            idade_gestacional = 2
        elif idade_gestacional == "3º Trimestre":
            idade_gestacional = 3
        elif idade_gestacional == "Idade gestacional ignorada":
            idade_gestacional = 4
        elif idade_gestacional == "Não gestante":
            idade_gestacional = 5
        elif idade_gestacional == "Não se aplica (Crianças)":
            idade_gestacional = 6
        else: 
            idade_gestacional = 9

        st.write("<p style='margin-top: 1rem'>Sintomas do paciente</p>", unsafe_allow_html=True)
        st.write("<hr style='margin: 0'>", unsafe_allow_html=True)
        
        febre = st.checkbox("Febre") 
        if febre:
            febre = 1
        else:
            febre = 2

        nausea = st.checkbox("Náusea")
        if nausea:
            nausea = 1
        else:
            nausea = 2

        conjuntivite = st.checkbox("Conjutivite")
        if conjuntivite:
            conjuntivite = 1
        else:
            conjuntivite = 2

        artralgia = st.checkbox("Artralgia")
        if artralgia:
            artralgia = 1
        else:
            artralgia = 2

        petequias = st.checkbox("Petequias")
        if petequias:
            petequias = 1
        else:
            petequias = 2

        leucopenia = st.checkbox("Leucopenia")
        if leucopenia:
            leucopenia = 1
        else:
            leucopenia = 2

        diabetes = st.checkbox("Diabetes")
        if diabetes:
            diabetes = 1
        else:
            diabetes = 2

        hepatopat = st.checkbox("Hepatopatias")
        if hepatopat:
            hepatopat = 1
        else:
            hepatopat = 2

        hipertensao = st.checkbox("Hipertensão arterial") 
        if hipertensao:
            hipertensao = 1
        else:
            hipertensao = 2

        if st.form_submit_button("Enviar"):

            result = clf.predict([[idade_gestacional, febre, nausea, conjuntivite, artralgia, petequias, leucopenia, diabetes, hepatopat, hipertensao]])[0]
            
            st.write("<h5 style='margin-top: 2rem'>Resultado:</h5>", unsafe_allow_html=True)

            if result == 1:
                st.write("<p style='align-text: center'>Provável chikungunya</p>", unsafe_allow_html=True)
            else:
                st.write("<p style='align-text: center'>Provável não chikungunya</p>", unsafe_allow_html=True)


    st.write("<h5>Métricas do modelo</h5>", unsafe_allow_html=True)

    df = pd.DataFrame({
        'Métrica': ['Accuracy', 'Precision (média macro)', 'Recall (média macro)', 'F1-score (média macro)'],
        'Valor': ['66,6%', '66,9%', '66,9%', '66,6%']
    })

    st.table(data=df)