import streamlit as st

class ManterClienteUI:
    def main():
        st.header("Cadastro de clientes")
        st.text_input("Nome")
        st.text_input("E-mail")
        st.text_input("Senha")
        st.text_input("Telefone")

        if st.button("Inserir"):
            pass #chame a função Inserir