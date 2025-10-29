import json
import datetime

class Corridas:
    def __init__(self, idTreino, idPessoa, data, distancia, tempo):
        self.__idTreino = idTreino
        self.__idPessoa = idPessoa
        self.__data = datetime.datetime.now() # str temporariamente
        self.__distancia = distancia
        self.__tempo = tempo
    
    def set_idTreino(self, novoIdTreino):
        if novoIdTreino == None:
            raise ValueError
        else:
            self.__idTreino = novoIdTreino
    
    def set_idPessoa(self, novoIdPessoa):
        if novoIdPessoa == None:
            raise ValueError
        else:
            self.__idPessoa = novoIdPessoa
    
    def set_data(self, novaData):
            novaData = datetime.datetime.now()
            self.__data = novaData
    
    def set_distancia(self, novaDistancia):
        if novaDistancia == None:
            raise ValueError
        else:
            self.__distancia = novaDistancia
    
    def set_tempo(self, novoTempo):
        if novoTempo == None:
            raise ValueError
        else:
            tempo_datetime = datetime.datetime.fromisoformat(novoTempo)
            tempo_datetime = datetime.timedelta()
            self.__tempo = tempo_datetime

    
    def get_idTreino(self):
        return self.__idTreino
    def get_idPessoa(self):
        return self.__idPessoa
    def get_data(self):
        return self.__data
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
        
    def pace(self):
        return self.__tempo // self.__distancia

class CorridasDAO:
    corridas = []

    @classmethod
    def inserir(cls, objetoCorrida):
        cls.abrir_json()
        idTreino = 0
        for verificador_id in cls.pessoas:
            if verificador_id.get_idTreino > idTreino:
                verificador_id.idTreino = idTreino + 1
        cls.corridas.append(objetoCorrida)
        cls.salvar_json()

    @classmethod
    def listar(cls):
        cls.abrir_json()
        return cls.corridas

    @classmethod
    def listar_menorPace(cls, p):
        p = Corridas.pace()
        cls.abrir_json()
        for aux in cls.corridas:
            if aux.get_tempo() == p:
                return aux

    @classmethod
    def abrir_json(cls):
        cls.clientes = []
        try:
            with open("corridas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Corridas.from_json(dic)
                    cls.corridas.append(c)
        except:
            pass          


    @classmethod
    def salvar_json(cls):
        with open("pessoas.json", mode="w") as arquivo:
            json.dump(cls.pessoas, arquivo, default=Corridas.to_json, indent=4)