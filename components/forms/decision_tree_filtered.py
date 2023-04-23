# MIALGIA, # 1 ou 2
# EXANTEMA, # 1 ou 2
# NAUSEA, # 1 ou 2
# ARTRALGIA, # 1 ou 2

# CLASSI_FIN

import pickle
import pandas as pd

with open('models_specialist/decision_tree_4.sav', 'rb')as f:
    clf = pickle.load(f)

def decision_tree_filtered_form(st):

    st.write("<h5>Teste</h5>", unsafe_allow_html=True)
    
    with st.form("Decision Tree - filtrado por um especialista", clear_on_submit=True):
        st.write("<p>Informações do paciente</p>", unsafe_allow_html=True)
        st.write("<hr style='margin: 0'>", unsafe_allow_html=True)

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

        if st.form_submit_button("Enviar"):

            result = clf.predict([[mialgia, exantema, nausea, artralgia]])[0]
            
            st.write("<h5 style='margin-top: 2rem'>Resultado:</h5>", unsafe_allow_html=True)

            if result == 1:
                st.write("<p style='align-text: center'>Provável chikungunya</p>", unsafe_allow_html=True)
            else:
                st.write("<p style='align-text: center'>Provável não chikungunya</p>", unsafe_allow_html=True)


    st.write("<h5>Métricas do modelo</h5>", unsafe_allow_html=True)
    df = pd.DataFrame({
        'Métrica': ['Accuracy', 'Precision (média macro)', 'Recall (média macro)', 'F1-score (média macro)'],
        'Valor': ['65,7%', '67,8%', '66,5%', '65,3%']
    })

    st.table(data=df)