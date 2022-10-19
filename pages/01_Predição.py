from components.forms.ada_boost import ada_boost_form
from components.forms.decision_tree import decision_tree_form
from components.forms.random_forest import random_forest_form
from components.header import header
import streamlit as st

header(st)

st.write("<h3 style='text-align: center;'>Diagnóstico de Chikungunya</h3>", unsafe_allow_html=True)

tab_dt, tab_rf, tab_ab = st.tabs(["Decision Tree", "Random Forest", "Ada Boost"])

with tab_dt:
    decision_tree_form(st)
with tab_rf:
    random_forest_form(st)
with tab_ab:
    ada_boost_form(st)

