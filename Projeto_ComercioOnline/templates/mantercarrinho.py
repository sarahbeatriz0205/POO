import streamlit as st
from views import View
from models.carrinho import Carrinho

class ManterCarrinhoUI:
    def main():

        st.header("Venha fazer suas compras aqui!")

        tab1, tab2= st.tabs(["Colocar produtos no meu carrinho", "Visualizar meu carrinho"])
        with tab1: ManterCarrinhoUI.inserir()
        with tab2: ManterCarrinhoUI.visualizar()

    def inserir():
        idCliente = st.session_state["cliente_id"]
        op = st.selectbox("Selecione o produto que você deseja", View.produto_listar())
        if op: 
            idProduto = op.get_idProduto()
            qtd = st.text_input("Qual a quantidade desse produto que você quer?")
            if st.button("Adicionar no carrinho"):
                c = Carrinho(idProduto, qtd, idCliente)
                View.inserir_produto(c)
                st.success("Item adicionado com sucesso!")
    
    def visualizar():
        idCliente = st.session_state["cliente_id"]
        v = View.visualizar_carrinho(idCliente)
        return v