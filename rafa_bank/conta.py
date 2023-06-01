from abc import ABC, abstractclassmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractclassmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f"(DEPÓSITO: {valor})")

    def detalhes(self, msg=""):
        print(f"Seu saldo é {self.saldo:.2f} {msg}")
