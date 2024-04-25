# Classes e Objetos para Dados
"""
Classe
"""

class Carro:                    # Classe
    def __init__(self):         # Método de inicialização
        print("Carro criado!")  # Escreve a mensagem
#%%
"""
Objetos
"""

class Carro:
    tipo = "sedan"

    def __init__(self):
        print("Carro criado!")

corolla = Carro()
civic = Carro()
#%%
"""
Atributo
"""

print(corolla.tipo)
#%%
class Carteira:
    pass
carteira1 = Carteira()
#%%
carteira1
#%%
"""
Atributos e Métodos
<objeto>.<atributo ou método>
"""

class Carteira:
    saldo = 0
#%%
c = Carteira()
#%%
c.saldo
#%%
# Parâmetros Especiais
"""
Conhecido por <self>, é obrigatório, e através dele se acessa os atributos e métodos da classe.
"""

class Carteira:
    saldo = 0

    def adicionar_fundos(self, valor):
        self.saldo += valor
        print('Operação de Crédito realizada com sucesso!')

    def remover_fundos(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Operação de Débito realizada com sucesso!')
        else:
            print('Saldo insuficiente!')
#%%
c = Carteira()
c.saldo
#%%
c.adicionar_fundos(50)
#%%
c.saldo
#%%
c.remover_fundos(25)
#%%
c.saldo
#%%
# UML
"""
Linguagem de Modelagem Unificada - Contém notação gráfica para documentar um projeto.
Diagrama de Classe:
|-----------------------|
|       CARTEIRA        |   --> Nome da classe
|-----------------------|
|       +saldo: int     |   --> Atributos
|-----------------------|
|   +adicionar_fundos() |   --> Metodos
|-----------------------|
|   +remover_fundos()   |
|-----------------------|
"""
#%%
# SP - Duas novas classes

class CartaoGold(Carteira):

    def calcular_cash_back(self,valor):
        return valor * 0.03

class CartaoPlatinum(Carteira):

    def calcular_cash_back(self,valor):
        return valor * 0.05
#%%
c = CartaoGold()
c.adicionar_fundos(100)
c.calcular_cash_back(c.saldo)
#%%
# Orientação a Objetos com Numpy
"""
Numpy é uma biblioteca open source para trabalhar com computação científica, pois oferece uma poderosa estrutura de
dados multidimensional que nos permite realizar operações de forma eficiente e rápida, incluindo matemática, lógica,
classificação, algebra linear, estatística, e muito mais.
"""

import numpy as np
minha_lista = [10, 20, 30]
meu_array = np.array(minha_lista)
print(meu_array)
#%%
print(type(meu_array))
#%%
meu_array.size
#%%
meu_array.max()
#%%
# Classe Abstrata
"""
Classe Abstrata permite que classes filhas herdem os atributos e métodos da classe pai. Classes derivadas das classes
abstratas são chamadas de classes concretas.
Classes abstratas utilizam o módulo abc (Abstração de Classes).
"""

from abc import ABC, abstractmethod


class CartaoBase(ABC):
    """Classe abstrata que representa um cartão médio"""

    @abstractmethod
    def calcular_cash_back(self, valor):
        pass
#%%
# Métodos e Heranças
"""
O método __init__ é chamado de construtor de classe, inicia objetos com atributos padrão que precisam obrigatoriamente
existir em um objeto de forma válida, ou que necessitam ser iniciados primeiro na execução do código.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#%%
x = Point(1, 2)
print(x.x)
#%%
# Herança de classes
"""
Herança de classes permite que classes filhas herdem os atributos e métodos da classe pai, abstraindo a lógica comum
em superclasss e gerenciando detalhes específicos na subclasse
"""


class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def obter_saldo(self):
        return self.saldo
#%%


class ContaPoupanca(Conta):
    def calcular_rendimentos(self):
        """Adiciona 0,05% ao saldo da conta"""
        self.saldo += self.saldo * 0.005
#%%
cp = ContaPoupanca(123, 456, 200)
cp.depositar(100)
cp.obter_saldo()
#%%
cp.sacar(50)
cp.obter_saldo()
#%%
cp.calcular_rendimentos()
cp.obter_saldo()
#%%
# Como instanciar uma classe que contenha um método abstrato?

from abc import ABC, abstractmethod
#%%
class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        raise NotImplementedError("Esse método precisa ser implementado!")
#%%
# Sobrescrevendo o método sacar
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def calcular_rendimentos(self):
        """Adiciona 0,05% ao saldo da conta"""
        self.saldo += self.saldo * 0.005
#%%
