from components.specialist_forms.ada_boost import ada_boost_form
from components.specialist_forms.decision_tree import decision_tree_form
from components.specialist_forms.gradient_boosting import gradient_boosting_form
from components.specialist_forms.knn import knn_form
from components.specialist_forms.random_forest import random_forest_form
from components.specialist_forms.xgb import xgb_form
from components.specialist_forms.svm import svm_form
from components.header import header
import streamlit as st

header(st)

st.write("<h3 style='text-align: center;'>Testes de modelos especialistas</h3>", unsafe_allow_html=True)

tab_ab, tab_dt, tab_rf, tab_gb, tab_knn, tab_xgb, tab_svm = st.tabs([
    "AdaBoost (Recomendado)", 
    "Decision Tree", 
    "Random Forest", 
    "Gradient Boosting", 
    "K-Nearest Neighbours", 
    "eXtreme Gradient Boosting", 
    "Support Vector Machine"
])

with tab_dt:
    decision_tree_form(st)
with tab_rf:
    random_forest_form(st)
with tab_gb:
    gradient_boosting_form(st)
with tab_knn:
    knn_form(st)
with tab_ab:
    ada_boost_form(st)
with tab_xgb:
    xgb_form(st)
with tab_svm:
    svm_form(st)

