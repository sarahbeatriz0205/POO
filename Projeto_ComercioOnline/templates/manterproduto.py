import streamlit as st
import pandas as pd
from time import time
from views import View

class ManterProdutoUI:
    def main():
        st.header("Cadastro de produtos")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        #with tab4: ManterProdutoUI.excluir()

    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto até o momento")
        else:
            list_dic = []
            for produto in produtos: list_dic.append(produto.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "nome", "email", "fone"])     

    def inserir():
        descricao = st.text_input("Descrição do produto")
        preco = st.text_input("Preço")
        estoque = st.text_input("Estoque atual")
        idCategoria = st.text_input("Id da categoria a qual pertence")
        if st.button("Inserir"):
            View.produto_inserir(descricao, preco, estoque, idCategoria)
            st.success("Produto adicionado com sucesso!")
            time.sleep(2)
            st.rerun()

    def atualizar():
        produtos = View.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto até o momento")
        else:
            op = st.sidebar.selectbox("Produtos", produtos)
            descricao = st.text_input("Nova descrição",  op.get_descricao())
            preco = st.text_input("Novo preço", op.get_preco())
            estoque = st.text_input("Novo estoque", op.get_estoque())
            idCategoria = st.text_input("Nova categoria", op.get_idCategoria())
            if st.button("Atualizar"):
                id = op.get_idProduto()
                View.produto_atualizar(id, descricao, preco, estoque, idCategoria)
                st.success("Produto atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        # selecionar um produto já existente e excluir
        pass
                
        