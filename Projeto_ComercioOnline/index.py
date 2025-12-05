from templates.manterclienteUI import ManterClienteUI
from templates.mantercategoria import ManterCategoriaUI
from templates.reajustarproduto import ReajusteProdutoUI
from templates.manterproduto import ManterProdutoUI
from templates.login import LoginUI
from templates.criar_conta import CriarContaUI
from templates.listarprodutosUI import ListarProdutosUI
from views import View
import streamlit as st

class IndexUI:
        def menu_visitante():
                op = st.selectbox("Entre no sistema ou crie sua conta", ["Entrar no sistema", 
                                                                        "Criar Conta"])
                if op == "Entrar no sistema": LoginUI.main()
                if op == "Criar Conta": CriarContaUI.main()
        def menu_admin():
                # st.sidebar.selectbox: caixa de seleção
                op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", 
                                        "Cadastro de Clientes", 
                                        "Cadastro de Produtos", 
                                        "Reajustar Produtos"])
                
                # ao clicar, direciono o usuário para a página correspode àquela opção
                st.session_state["opcao"].append(op)
                if op == "Cadastro de Categorias": ManterCategoriaUI.main()
                if op == "Cadastro de Clientes": ManterClienteUI.main()
                if op == "Cadastro de Produtos": ManterProdutoUI.main()
                if op == "Reajustar Produtos": ReajusteProdutoUI.main()
        
        def menu_cliente():
                op = st.sidebar.selectbox("Menu", ["Listar produtos",
                                        "Inserir produtos no carrinho",
                                        "Visualizar o carrinho",
                                        "Comprar produtos do carrinho",
                                        "Listar minhas compras",
                                        "Favoritar produtos",
                                        "Desfavoritar produtos",
                                        "Mostrar meus favoritos"])
                if op == "Listar produtos": ListarProdutosUI.main()
                if op == "Inserir produtos no carrinho": pass # página que liste os produtos, permita seleção de produtos


        def sidebar():
                if "cliente_id" not in st.session_state: IndexUI.menu_visitante()
                else:
                        admin = st.session_state["cliente_nome"] == "admin"
                        if admin: IndexUI.menu_admin()
                        else: IndexUI.menu_cliente()
                        IndexUI.sair_do_sistema() 

        def sair_do_sistema():
                if st.sidebar.button("Sair"):
                        del st.session_state["cliente_id"]
                        del st.session_state["cliente_nome"]
                        st.rerun()
                
        def main():
                #View.cliente_criar_admin() # o que receber aqui?
                IndexUI.sidebar() 


IndexUI.main()