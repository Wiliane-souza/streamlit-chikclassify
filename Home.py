from components.header import header
import streamlit as st

st.set_page_config(page_title="CO Diagnóstico", page_icon="./assets/img/favicon.png")

header(st)

st.write("<h3 style='text-align: center;'> Sua assistente no diagnóstico da Chikungunya!</h3>", unsafe_allow_html=True)

# TODO: atualizar texto de acordo com atributos dos feature selection de cada modelo

st.write("<p style='text-align: justify;'> O CO Diagnóstico é uma plataforma que utiliza aprendizado de \
    máquina para dar suporte a profissionais de saúde na investigação \
    e classificação de casos de Chikungunya. Para isso, utiliza a técnicas como Decision Tree, Random Forest\
    Ada Boost, KNN e outros. É utilizada\
    uma base com dados reais de 140.516 pacientes brasileiros, coletados do Sistema de Informação de \
    Agravos de Notificação (SIAN). Utiliza 8 atributos, que consistem em sexo do paciente e sintomas clínicos \
    como febre, mialgia, cefaleia, exantema, artrite, artralgia e dor retro abdominal; \
    além da classe alvo (Chikungunya ou Outras doenças). O modelo melhor modelo, que atualmente utiliza \
    Decision Tree, obteve acurácia de 83,7% \
    e precisão, sensibilidade e F1-score de 84%.</p>", unsafe_allow_html=True)

