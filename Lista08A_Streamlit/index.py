import streamlit as st
from equacao import EquacaoGrauDois

st.header("Calculadora de equação de 2º grau")
a = st.text_input("Insira o valor de A")
b = st.text_input("Insira o valor de B")
c = st.text_input("Insira o valor de C")
if st.button("Calcular"):
    eq = EquacaoGrauDois(int(a), int(b), int(c))
    st.write(f"Delta = {eq.calc_delta()}")
    st.write(f"x1 = {eq.x1()}")
    st.write(f"x2 = {eq.x2()}")
