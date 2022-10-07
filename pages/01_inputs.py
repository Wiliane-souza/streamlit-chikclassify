from tabnanny import check
import streamlit as st

st.title("DotLab - Workshop")

textInput = st.text_input("Text Input", placeholder="Your name")
st.write(textInput)

textArea = st.text_area("Text Area", placeholder="About you")
st.write(textArea)

numberInput = st.number_input("Number Input", min_value=0, max_value=150, value=18, step=2)
st.write(numberInput)

dateInput = st.date_input("Date Input")
st.write(dateInput)

checkbox = st.checkbox("Checkbox")
st.write(checkbox)

radio = st.radio("Sexo", ["Masculino", "Feminino"])
st.write(radio)

selectBox = st.selectbox("Cidade", ["Caruaru", "Recife"])
st.write(selectBox)

multiselectBox = st.multiselect("Radio", ["Caruaru", "Recife"])
st.write(multiselectBox)

slider = st.slider("Slider", min_value=0, max_value=10)
st.write(slider)

if st.button("Button"):
    st.write("Button clicked")