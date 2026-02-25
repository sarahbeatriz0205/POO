import streamlit as st
import pandas as pd
from retangulo import Retangulo

st.header("Calculadora de área de um retângulo")
b = st.text_input("Informe a base")
h = st.text_input("Informe a altura")
if st.button("Calcular"):
    r = Retangulo(float(b), float(h))
    st.write(f"Informações inseridas: {r}")
    st.write(f"Área = {r.area()}")
    st.write(f"Diagonal = {r.diagonal()}")

    df = pd.DataFrame(
        {
            "x": [1, 3, 5],
            "y": [4, 5, 2],
        }
    )
    st.line_chart(df, x="x", y="y")