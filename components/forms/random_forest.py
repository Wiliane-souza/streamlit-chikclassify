
# CS_SEXO, FEBRE, MIALGIA, CEFALEIA, EXANTEMA, ARTRITE, ARTRALGIA, DOR_RETRO, CLASSI_FIN

import pickle

with open('model/model.sav', 'rb')as f:
    clf = pickle.load(f)

def random_forest_form(st):
    with st.form("Random Forest", clear_on_submit=True):
        st.write("<p>Informações do paciente</p>", unsafe_allow_html=True)
        st.write("<hr style='margin: 0'>", unsafe_allow_html=True)

        sexo = st.selectbox("Sexo", ["Não informado", "Masculino", "Feminino"])
        if sexo == "Masculino":
            sexo = 1
        elif sexo == "Feminino":
            sexo = 2
        else: 
            sexo = 0

        st.write("<p style='margin-top: 1rem'>Sintomas do paciente</p>", unsafe_allow_html=True)
        st.write("<hr style='margin: 0'>", unsafe_allow_html=True)
        
        febre = st.checkbox("Febre")
        if febre:
            febre = 1

        mialgia = st.checkbox("Mialgia")
        if mialgia:
            mialgia = 1

        cefaleia = st.checkbox("Cefaleia")
        if cefaleia:
            cefaleia = 1

        exantema = st.checkbox("Exantema")
        if exantema:
            exantema = 1

        artrite = st.checkbox("Artrite")
        if artrite:
            artrite = 1

        artralgia = st.checkbox("Artralgia")
        if artralgia:
            artralgia = 1

        dor_retro = st.checkbox("Dor retro-orbitária")
        if dor_retro:
            dor_retro = 1

        if st.form_submit_button("Enviar"):

            result = clf.predict([[sexo, febre, mialgia, cefaleia, exantema, artrite, artralgia, dor_retro]])[0]

            
            st.write("<h5 style='margin-top: 2rem'>Resultado:</h5>", unsafe_allow_html=True)

            if result == 1:
                st.write("<p style='align-text: center'>Provável chikungunya</p>", unsafe_allow_html=True)
            else:
                st.write("<p style='align-text: center'>Provável não chikungunya</p>", unsafe_allow_html=True)