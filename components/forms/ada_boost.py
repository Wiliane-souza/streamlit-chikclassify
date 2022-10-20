
# CS_SEXO, FEBRE, MIALGIA, CEFALEIA, EXANTEMA, ARTRITE, ARTRALGIA, DOR_RETRO, CLASSI_FIN

import pickle

with open('model/model.sav', 'rb')as f:
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


"NU_NOTIFIC",
"TP_NOT",
"# DT_NOTIFIC",
"# SEM_NOT",
"# NU_ANO",
"SG_UF_NOT",
"ID_MUNICIP",
"ID_REGIONA",
"ID_UNIDADE",
"# DT_SIN_PRI",
"SEM_PRI",
"# DT_NASC",
"NU_IDADE_N",
"CS_SEXO",
"CS_GESTANT",
"CS_RACA",
"CS_ESCOL_N",
"SG_UF",
"ID_MN_RESI",
"ID_RG_RESI",
"ID_DISTRIT",
"ID_BAIRRO",
"NM_BAIRRO",
"CS_ZONA",
"ID_PAIS",
"# DT_INVEST",
"ID_OCUPA_N",
"FEBRE",
"MIALGIA",
"CEFALEIA",
"EXANTEMA",
"VOMITO",
"NAUSEA",
"DOR_COSTAS",
"CONJUNTVIT",
"ARTRITE",
"ARTRALGIA",
"PETEQUIA_N",
"LEUCOPENIA",
"LACO",
"DOR_RETRO",
"DIABETES",
"HEMATOLOG",
"HEPATOPAT",
"RENAL",
"HIPERTENSA",
"ACIDO_PEPT",
"AUTO_IMUNE",
"# DT_CHIK_S1",
"# DT_CHIK_S2",
"# DT_PRNT",
"RES_CHIKS1",
"RES_CHIKS2",
"RESUL_PRNT",
"# DT_SORO",
"RESUL_SORO",
"# DT_NS1",
"RESUL_NS1",
"# DT_VIRAL",
"RESUL_VI_N",
"# DT_PCR",
"RESUL_PCR_",
"SOROTIPO",
"HISTOPA_N",
"IMUNOH_N",
"HOSPITALIZ",
"# DT_INTERNA",
"UF",
"MUNICIPIO",
"TPAUTOCTO",
"COUFINF",
"COPAISINF",
"COMUNINF",
"CODISINF",
"CO_BAINF",
"NOBAIINF",
"CLASSI_FIN",
"CRITERIO",
"DOENCA_TRA",
"CLINC_CHIK",
"EVOLUCAO",
"# DT_OBITO",
"# DT_ENCERRA",
"ALRM_HIPOT",
"ALRM_PLAQ",
"ALRM_VOM",
"ALRM_SANG",
"ALRM_HEMAT",
"ALRM_ABDOM",
"ALRM_LETAR",
"ALRM_HEPAT",
"ALRM_LIQ",
"# DT_ALRM",
"GRAV_PULSO",
"GRAV_CONV",
"GRAV_ENCH",
"GRAV_INSUF",
"GRAV_TAQUI",
"GRAV_EXTRE",
"GRAV_HIPOT",
"GRAV_HEMAT",
"GRAV_MELEN",
"GRAV_METRO",
"GRAV_SANG",
"GRAV_AST",
"GRAV_MIOC",
"GRAV_CONSC",
"GRAV_ORGAO",
"# DT_GRAV",
"EPISTAXE",
"GENGIVO",
"METRO",
"PETEQUIAS",
"HEMATURA",
"SANGRAM",
"LACO_N",
"PLASMATICO",
"EVIDENCIA",
"PLAQ_MENOR",
# COMPLICA