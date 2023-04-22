# CS_GESTANT, # 1-3 (trimestre), 4-idade gestacional ignorado, 5- Não gestante, 6- Não se aplica, 9-ignorado
# MIALGIA, # 1 ou 2
# EXANTEMA, # 1 ou 2
# NAUSEA, # 1 ou 2
# ARTRALGIA, # 1 ou 2
# LEUCOPENIA, # 1 ou 2
# DIABETES, # 1 ou 2
# HEMATOLOG, # 1 ou 2
# HEPATOPAT, # 1 ou 2
# AUTO_IMUNE, # 1 ou 2
# CLASSI_FIN

import pickle
import pandas as pd

with open('models/decision_tree.sav', 'rb')as f:
    clf = pickle.load(f)

def decision_tree_form(st):

    st.write("<h5>Teste</h5>", unsafe_allow_html=True)
    
    with st.form("Decision Tree", clear_on_submit=True):
        st.write("<p>Informações do paciente</p>", unsafe_allow_html=True)
        st.write("<hr style='margin: 0'>", unsafe_allow_html=True)

        idade_gestacional = st.selectbox("Idade Gestacional", [
            "Ignorado",
            "1º Trimestre",
            "2º Trimestre",
            "3º Trimestre",
            "Idade gestacional ignorada",
            "Mulher não gestante",
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
        elif idade_gestacional == "Mulher não gestante":
            idade_gestacional = 5
        elif idade_gestacional == "Não se aplica (Crianças)":
            idade_gestacional = 6
        else: 
            idade_gestacional = 9

        st.write("<p style='margin-top: 1rem'>Sintomas do paciente</p>", unsafe_allow_html=True)
        st.write("<hr style='margin: 0'>", unsafe_allow_html=True)

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

        artralgia = st.checkbox("Artralgia") 
        if artralgia:
            artralgia = 1
        else:
            artralgia = 2

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

        hematolog = st.checkbox("Doenças hematológicas") 
        if hematolog:
            hematolog = 1
        else:
            hematolog = 2

        hepatopat = st.checkbox("Hepatopatias") 
        if hepatopat:
            hepatopat = 1
        else:
            hepatopat = 2

        auto_imune = st.checkbox("Doenças auto-imunes") 
        if auto_imune:
            auto_imune = 1
        else:
            auto_imune = 2

        if st.form_submit_button("Enviar"):

            result = clf.predict([[idade_gestacional, mialgia, exantema, nausea, artralgia, leucopenia, diabetes, hematolog, hepatopat, auto_imune]])[0]
            
            st.write("<h5 style='margin-top: 2rem'>Resultado:</h5>", unsafe_allow_html=True)

            if result == 1:
                st.write("<p style='align-text: center'>Provável chikungunya</p>", unsafe_allow_html=True)
            else:
                st.write("<p style='align-text: center'>Provável não chikungunya</p>", unsafe_allow_html=True)


    st.write("<h5>Métricas do modelo</h5>", unsafe_allow_html=True)
    df = pd.DataFrame({
        'Métrica': ['Accuracy', 'Precision (média macro)', 'Recall (média macro)', 'F1-score (média macro)'],
        'Valor': ['66,2%', '66,3%', '66,4%', '66,2%']
    })

    st.table(data=df)