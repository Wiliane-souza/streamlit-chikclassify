import streamlit as st


st.title('Gráficos')

tab1, tab2, tab3 = st.tabs(["Aba 1", "Aba 2", "Aba 3"])

tab1.write("### teste")
tab2.write("### teste")
tab3.write("### teste")


st.sidebar.write("### Sidebar")