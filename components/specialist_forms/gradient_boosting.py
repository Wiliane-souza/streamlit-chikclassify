import pickle
import pandas as pd

with open('models_specialist/gradient_boosting.sav', 'rb')as f:
    clf = pickle.load(f)

def gradient_boosting_form(st):

    st.write("<h5>Teste</h5>", unsafe_allow_html=True)
    
    with st.form("Gradient Boosting", clear_on_submit=True):

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

        cefaleia = st.checkbox("Cefaleia") 
        if cefaleia:
            cefaleia = 1
        else:
            cefaleia = 2

        exantema = st.checkbox("Exantema") 
        if exantema:
            exantema = 1
        else:
            exantema = 2
        
        vomito = st.checkbox("Vômito") 
        if vomito:
            vomito = 1
        else:
            vomito = 2

        nausea = st.checkbox("Náusea") 
        if nausea:
            nausea = 1
        else:
            nausea = 2

        dor_costas = st.checkbox("Dor nas costas") 
        if dor_costas:
            dor_costas = 1
        else:
            dor_costas = 2

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

        dor_retro = st.checkbox("Dor retroorbital")
        if dor_retro:
            dor_retro = 1
        else:
            dor_retro = 2

        if st.form_submit_button("Enviar"):

            result = clf.predict([[febre, mialgia, cefaleia, exantema, vomito, nausea, dor_costas, conjutivite, artrite, artralgia, petequias, dor_retro]])[0]
            
            st.write("<h5 style='margin-top: 2rem'>Resultado:</h5>", unsafe_allow_html=True)

            if result == 1:
                st.write("<p style='align-text: center'>Provável chikungunya</p>", unsafe_allow_html=True)
            else:
                st.write("<p style='align-text: center'>Provável não chikungunya</p>", unsafe_allow_html=True)


    st.write("<h5>Métricas do modelo</h5>", unsafe_allow_html=True)

    df = pd.DataFrame({
        'Métrica': ['Accuracy', 'Precision (média macro)', 'Recall (média macro)', 'F1-score (média macro)'],
        'Valor': ['65,4%', '65,9%', '65,8%', '65,4%']
    })

    st.table(data=df)