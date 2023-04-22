from components.header import header
import streamlit as st
import pandas as pd

header(st)

st.write("<h3 style='text-align: center;'> Sua assistente no diagnóstico da Chikungunya!</h3>", unsafe_allow_html=True)

st.write("<p style='text-align: justify;'> \
    O ChikClassify é uma plataforma para fins educativos que expõe modelos de aprendizado de máquina \
    criados com o objetivo de dar suporte a profissionais de saúde na investigação \
    e classificação de casos de Chikungunya. Para isso, utiliza classificadores como Decision Tree, Random Forest, Gradient Boosting\
    Ada Boost, KNN, XgBoost e SVM. É utilizada\
    uma base com dados reais de mais de 140 mil pacientes brasileiros, coletados do Sistema de Informação de \
    Agravos de Notificação (SINAN) e do Portal de Dados Abertos do Recife (PDA). Utiliza 10 atributos, que consistem \
    em dados sobre o paciente e sintomas clínicos. \
    O melhor modelo, que atualmente utiliza o classificador Decision Tree, obteve as seguintes métricas:", unsafe_allow_html=True)

df = pd.DataFrame({
    'Métrica': ['Acurácia', 'Precisão', 'Sensibilidade', 'F1-score'],
    'Valor': ['66,2%', '66,3%', '66,4%', '66,2%']
})

st.table(data=df)