import streamlit as st

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de categorias")
        st.text_input("Descrição da categoria")

        if st.button("Inserir"):
            pass #chame a função Inserir