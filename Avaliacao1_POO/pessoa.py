from datetime import datetime
import json

class Pessoa:
    def __init__(self, idPessoa, nome, nascimento):
        self.__idPessoa = idPessoa
        self.__nome = nome
        self.__nascimento = nascimento


    
    def set_idPessoa(self, novoidPessoa):
        if novoidPessoa == None:
            raise ValueError
        else:
            self.__idPessoa = novoidPessoa
    def set_nome(self, novoNome):
        if novoNome == None:
            raise ValueError
        else:
            self.__idPessoa = novoNome
    def set_nascimento(self, novoNascimento):
        if novoNascimento == None:
            raise ValueError
        else:
            self.__idPessoa = novoNascimento

    


    def get_idPessoa(self):
        return self.__idPessoa
    def get_nome(self):
        return self.__nome
    def get_nascimento(self):
        return self.__nascimento
    


    
    def __str__(self):
        return f"{self.__idPessoa} - {self.__nome} - {self.__nascimento}"

    def to_json(self):
        return {"idPessoa" : self.__idPessoa, "nome" : self.__nome, "data_de_nascimento" : self.__nascimento}
    
    @staticmethod
    def from_json(dic):
        return Pessoa(dic["idPessoa"], dic["nome"], dic["data_de_nascimento"])


class PessoaDAO:
    pessoas = []

    @classmethod
    def inserir(cls, objetoPessoa):
        cls.abrir_json()
        idPessoa = 0
        for verificador_id in cls.pessoas:
            if verificador_id.get_idPessoa() > idPessoa:
                verificador_id.idPessoa = idPessoa + 1
        cls.pessoas.append(objetoPessoa)
        cls.salvar_json()

    @classmethod
    def listar(cls):
        cls.abrir_json()
        return cls.pessoas

    @classmethod
    def abrir_json(cls):
        cls.pessoas = []
        try:
            with open("pessoas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Pessoa.from_json(dic)
                    cls.pessoas.append(c)
        except:
            pass          


    @classmethod
    def salvar_json(cls):
        with open("pessoas.json", mode="w") as arquivo:
            json.dump(cls.pessoas, arquivo, default=Pessoa.to_json, indent=4)