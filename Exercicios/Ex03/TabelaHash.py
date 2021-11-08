# TABELA HASH EM ENCADEAMENTO SEPARADO
import os

class Conexao:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
    def obtemDado(self):
        return self.dado
    def mostrarConexao(self):
        print(self.dado)

class ListaOrdenada:
    def __init__(self):
        self.primeiro = None
    def inserir(self,conexao):
        chave = conexao.obtemDado()
        anterior = None
        atual = self.primeiro
        while atual 1 = None and chave > atual.obtemDado():
            anterior = atual
            atual = atual.proximo
        if anterior == None:
            self.primeiro = conexao
        else:
            anterior.proximo = conexao
            conexao.proximo = atual





