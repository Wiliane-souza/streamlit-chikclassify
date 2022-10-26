
# [
#     'CS_SEXO', #
#     'CS_GESTANT',  #
#     'FEBRE', #
#     'MIALGIA', #
#     'EXANTEMA', #
#     'NAUSEA', #
#     'ARTRITE', #
#     'ARTRALGIA',  # 
#     'DIABETES', #
#     'RENAL' #
# ]

import pickle

with open('model/ada_boost.sav', 'rb')as f:
    clf = pickle.load(f)

def ada_boost_form(st):
    with st.form("Ada Boost", clear_on_submit=True):
        st.write("<p>Informações do paciente</p>", unsafe_allow_html=True)
        st.write("<hr style='margin: 0'>", unsafe_allow_html=True)

        sexo = st.selectbox("Sexo", ["Não informado", "Masculino", "Feminino"])
        if sexo == "Masculino":
            sexo = 1
        elif sexo == "Feminino":
            sexo = 2
        else: 
            sexo = 0

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

        exantema = st.checkbox("Exantema")
        if exantema:
            exantema = 1
        else:
            exantema = 2

        nausea = st.checkbox("Nausea") 
        if nausea:
            nausea = 1
        else:
            nausea = 2

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

        renal = st.checkbox("Doença renal crônica")
        if renal:
            renal = 1
        else:
            renal = 2

        if st.form_submit_button("Enviar"):

            # [ CS_SEXO', 'CS_GESTANT', 'FEBRE', 'MIALGIA', 'EXANTEMA', 'NAUSEA',
            #     'ARTRITE', 'ARTRALGIA', 'DIABETES', 'RENAL' ]

            result = clf.predict([[sexo, idade_gestacional, febre, mialgia, exantema, nausea, artrite, artralgia, diabetes, renal]])[0]

            st.write("<h5 style='margin-top: 2rem'>Resultado:</h5>", unsafe_allow_html=True)

            if result == 1:
                st.write("<p style='align-text: center'>Provável chikungunya</p>", unsafe_allow_html=True)
            else:
                st.write("<p style='align-text: center'>Provável não chikungunya</p>", unsafe_allow_html=True)
    
    st.write("<h5>Métricas desse modelo: </h5>", unsafe_allow_html=True)
    st.write("<p>Acurácia: 84.21%</p>", unsafe_allow_html=True)
    st.write("<p>Precisão: 83%</p>", unsafe_allow_html=True)
    st.write("<p>Sensibilidade: 85%</p>", unsafe_allow_html=True)
    st.write("<p>F1-score: 84%</p>", unsafe_allow_html=True)