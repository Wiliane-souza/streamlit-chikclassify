# [
#     'CS_GESTANT',  #
#     'FEBRE', #
#     'NAUSEA', #
#     'CONJUTIVITE', #
#     'ARTRITE', #
#     'ARTRALGIA',  # 
#     'PETEQUIA_N',  # 
#     'LEUCONPENIA',  # 
#     'DOR_RETRO',  # 
#     'HEMATOLOG', #
#     'RENAL' #
# ]

import pickle
import pandas as pd

with open('models/adaBoost.sav', 'rb')as f:
    clf = pickle.load(f)

def ada_boost_form(st):

    st.write("<h5>Teste</h5>", unsafe_allow_html=True)
    
    with st.form("Ada Boost", clear_on_submit=True):
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

        nausea = st.checkbox("Nausea") 
        if nausea:
            nausea = 1
        else:
            nausea = 2

        conjutivite = st.checkbox("Conjutivite") 
        if conjutivite:
            conjutivite = 1
        else:
            conjutivite = 2

        artrite = st.checkbox("Artrite") 
        if artrite:
            artrite = 1
        else:
            artrite = 2

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

        dor_retro = st.checkbox("Dor retroorbital")
        if dor_retro:
            dor_retro = 1
        else:
            dor_retro = 2

        hematolog = st.checkbox("Doenças hematológicas")
        if hematolog:
            hematolog = 1
        else:
            hematolog = 2

        if st.form_submit_button("Enviar"):

            result = clf.predict([[idade_gestacional, febre, nausea, conjutivite, artrite, artralgia, petequias, leucopenia, dor_retro, hematolog]])[0]

            st.write("<h5 style='margin-top: 2rem'>Resultado:</h5>", unsafe_allow_html=True)

            if result == 1:
                st.write("<p style='align-text: center'>Provável chikungunya</p>", unsafe_allow_html=True)
            else:
                st.write("<p style='align-text: center'>Provável não chikungunya</p>", unsafe_allow_html=True)


    st.write("<h5>Métricas do modelo</h5>", unsafe_allow_html=True)

    df = pd.DataFrame({
        'Métrica': ['Accuracy', 'Precision (média macro)', 'Recall (média macro)', 'F1-score (média macro)'],
        'Valor': ['67,8%', '67,7%', '67,8%', '67,7%']
    })

    st.table(data=df)