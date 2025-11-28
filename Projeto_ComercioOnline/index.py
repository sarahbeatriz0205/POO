from templates.manterclienteUI import ManterClienteUI
from templates.mantercategoria import ManterCategoriaUI
from templates.reajustarproduto import ReajusteProdutoUI
from templates.manterproduto import ManterProdutoUI
import streamlit as st

class IndexUI:
        def menu_admin():
            # st.sidebar.selectbox: caixa de seleção
            op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", 
                                    "Cadastro de Clientes", 
                                    "Cadastro de Produtos", 
                                    "Reajustar Produtos"])
            
            # ao clicar, direciono o usuário para a página correspode àquela opção
            if op == "Cadastro de Categorias": ManterCategoriaUI.main()
            if op == "Cadastro de Clientes": ManterClienteUI.main()
            if op == "Cadastro de Produtos": ManterProdutoUI.main()
            if op == "Reajustar Produtos": ReajusteProdutoUI.main()

        def sidebar():
            IndexUI.menu_admin()


IndexUI.sidebar()