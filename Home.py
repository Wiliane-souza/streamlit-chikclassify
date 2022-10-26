from components.header import header
import streamlit as st

header(st)

st.write("<h3 style='text-align: center;'> Sua assistente no diagnóstico da Chikungunya!</h3>", unsafe_allow_html=True)

# TODO: atualizar texto de acordo com atributos dos feature selection de cada modelo

st.write("<p style='text-align: justify;'> O CO Diagnóstico é uma plataforma que utiliza aprendizado de \
    máquina para dar suporte a profissionais de saúde na investigação \
    e classificação de casos de Chikungunya. Para isso, utiliza a técnicas como Decision Tree, Random Forest\
    Ada Boost, KNN e outros. É utilizada\
    uma base com dados reais de 140.516 pacientes brasileiros, coletados do Sistema de Informação de \
    Agravos de Notificação (SIAN). Utiliza 10 atributos, que consistem dados sobre o paciente e sintomas clínicos. \
    O modelo melhor modelo, que atualmente utiliza Random Forest, obteve as seguintes métricas:", unsafe_allow_html=True)

st.write("<span>Acurácia: 84.61%</span>", unsafe_allow_html=True)
st.write("<span>Precisão: 85%</span>", unsafe_allow_html=True)
st.write("<span>Sensibilidade: 84%</span>", unsafe_allow_html=True)
st.write("<span>F1-score: 84%</span>", unsafe_allow_html=True)

