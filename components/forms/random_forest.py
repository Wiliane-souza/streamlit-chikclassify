
# [
#     'CS_GESTANT', #  1-3 (trimestre), 4-idade gestacional ignorado, 5- Não gestante, 6- Não se aplica, 9-ignorado
#     'FEBRE', # 1 ou 2
#     'MIALGIA',  # 1 ou 2
#     'DOR_COSTAS', # 1 ou 2
#     'ARTRITE',  # 1 ou 2
#     'ARTRALGIA', # 1 ou 2
#     'DIABETES', # 1 ou 2
#     'GENGIVO', # 1 ou 2
#     'METRO', # 1 ou 2
#     'PETEQUIAS', # 1 ou 2
#     'CLASSI_FIN'
# ]

import pickle

with open('model/random_forest.sav', 'rb')as f:
    clf = pickle.load(f)

def random_forest_form(st):
    with st.form("Random Forest", clear_on_submit=True):
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

        mialgia = st.checkbox("Mialgia")
        if mialgia:
            mialgia = 1
        else:
            mialgia = 2

        dor_costas = st.checkbox("Dor nas costas")
        if dor_costas:
            dor_costas = 1
        else:
            dor_costas = 2

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

        diabetes = st.checkbox("Diabetes")
        if diabetes:
            diabetes = 1
        else:
            diabetes = 2

        gengivo = st.checkbox("Gengivorragia")
        if gengivo:
            gengivo = 1
        else:
            gengivo = 2

        metro = st.checkbox("Metrorragia")
        if metro:
            metro = 1
        else:
            metro = 2

        petequias = st.checkbox("Petequias")
        if petequias:
            petequias = 1
        else:
            petequias = 2

        if st.form_submit_button("Enviar"):

            # ['CS_GESTANT', 'FEBRE', 'MIALGIA', 'DOR_COSTAS', 'ARTRITE', 'ARTRALGIA',
            # 'DIABETES', 'GENGIVO', 'METRO', 'PETEQUIAS', 'CLASSI_FIN']

            result = clf.predict([[idade_gestacional, febre, mialgia, dor_costas, artrite, artralgia, diabetes, gengivo, metro, petequias]])[0]
            
            st.write("<h5 style='margin-top: 2rem'>Resultado:</h5>", unsafe_allow_html=True)

            if result == 1:
                st.write("<p style='align-text: center'>Provável chikungunya</p>", unsafe_allow_html=True)
            else:
                st.write("<p style='align-text: center'>Provável não chikungunya</p>", unsafe_allow_html=True)
    
    st.write("<h5>Métricas desse modelo: </h5>", unsafe_allow_html=True)
    st.write("<p>Acurácia: 84.61%</p>", unsafe_allow_html=True)
    st.write("<p>Precisão: 85%</p>", unsafe_allow_html=True)
    st.write("<p>Sensibilidade: 84%</p>", unsafe_allow_html=True)
    st.write("<p>F1-score: 84%</p>", unsafe_allow_html=True)