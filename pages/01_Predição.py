from components.forms.ada_boost import ada_boost_form
from components.forms.decision_tree import decision_tree_form
from components.forms.decision_tree_filtered import decision_tree_filtered_form
from components.forms.gradient_boosting import gradient_boosting_form
from components.forms.knn import knn_form
from components.forms.random_forest import random_forest_form
from components.forms.xgb import xgb_form
from components.forms.svm import svm_form
from components.header import header
import streamlit as st

header(st)

st.write("<h3 style='text-align: center;'>Testes de modelos</h3>", unsafe_allow_html=True)

tab_dt, tab_dt_f, tab_rf, tab_gb, tab_knn, tab_ab, tab_xgb, tab_svm = st.tabs([
    "Decision Tree", 
    "Decision Tree (filtrado)", 
    "Random Forest", 
    "Gradient Boosting", 
    "K-Nearest Neighbours", 
    "AdaBoost", 
    "eXtreme Gradient Boosting", 
    "Support Vector Machine"
])

with tab_dt:
    decision_tree_form(st)
with tab_dt_f:
    decision_tree_filtered_form(st)
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

