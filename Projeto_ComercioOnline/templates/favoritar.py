import streamlit as st
from views import View
from models.favorito import Favorito

class ManterFavoritoUI:
    def main():

        st.header("Favoritar produtos")

        tab1, tab2 = st.tabs(["Favoritar", "Desfavoritar"])
        with tab1: ManterFavoritoUI.favoritar()
        with tab2: ManterFavoritoUI.desfavoritar()

    def favoritar():
        idCliente = st.session_state["cliente_id"]
        op = st.selectbox("Selecione o produto que você deseja favoritar", View.produto_listar())
        if op: 
            idProduto = op.get_idProduto()
            if st.button("Curtir"):
                c = Favorito(idProduto, idCliente)
                View.favoritar(c)
                st.success("Item favoritado com sucesso!")

    def desfavoritar():
        idCliente = st.session_state["cliente_id"]
        op = st.selectbox("Selecione o produto que você deseja desfavoritar", View.produtos_favoritos(idCliente))
        if op: 
            idProduto = op.get_idProduto()
            if st.button("Desfavoritar"):
                c = Favorito(idProduto, idCliente)
                View.desfavoritar(c)
                st.success("Item desfavoritado com sucesso!")