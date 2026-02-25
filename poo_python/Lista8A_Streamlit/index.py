import streamlit as st
from equacao import EquacaoGrauDois
import pandas as pd

st.header("Calculadora de equação de 2º grau")
a = st.text_input("Insira o valor de A")
b = st.text_input("Insira o valor de B")
c = st.text_input("Insira o valor de C")
if st.button("Calcular"):
    eq = EquacaoGrauDois(int(a), int(b), int(c))
    st.write(f"Delta = {eq.calc_delta()}")
    st.write(f"x1 = {eq.x1()}")
    st.write(f"x2 = {eq.x2()}")


    p = eq.ponto_inflexao()
    xmin = p - 10
    xmax = p + 10
    npontos = 50
    dist = (xmax - xmin) / (npontos - 1)

    px = []
    py = []

    x = xmin
    while x <= xmax:
        y = eq.y(x)
        px.append(x)
        py.append(y)
        x += dist

    df = pd.DataFrame({"x": px, "y": py})
    st.line_chart(df, x="x", y="y")