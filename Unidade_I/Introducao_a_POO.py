# Programação para Ciência de Dados
"""
Paradigma de Programação
> Paradigma de programação é a forma de escrita de um determinado código, desde que ele aceite. Existem linguagens que
aceitam mais de um paradigma de programação. Um deles, a programação orientada a objetos, apresenta como uma das
principais características: a reutilização de código. Isso é possível, por exemplo, pela construção de classes.
Outro exemplo é o paradigma estruturado que tem como principal característica seguir sequência.

A programação orientada a objetos tem como pilar a:
1 - Abstração;
2 - Encapsulamento;
3 - Herança;
4 - Polimorfismo.

Abstração:
> A abstração significa definir e focar no que é necessário no desenvolvimento.
Encapsulamento:
> O encapsulamento é o processo de proteger os dados de uma classe.
Herança:
> A herança permite que uma classe herde atributos e métodos de outras classes.
Polimorfismo:
> O polimorfismo diz respeito a capacidade da linguagem de programação de processar objetos de formas diferentes
a depender do seu tipo de dado ou classe.
"""

# Bibliotecas
"""
Pandas
> Biblioteca para manipulação de dados.
Numpy
> Biblioteca para manipulação de arrays e funções matemáticas.
Matplotlib
> Biblioteca para plotagem de dados.
"""

# Estruturas
"""
Listas
> Lista de dados. ['a', 'b', 'c']
Tuplas
> Tupla de dados. ('a', 'b', 'c')
Conjuntos
> Conjunto de dados. {'a', 'b', 'c'}
Dicionários
> Dicionário de dados. {'a': 1, 'b': 2, 'c': 3}

Condição
> if
> elif
> else
Repetição
> for
> while
Try e Except
> try
> except
"""

#%%
# Exercícios
import pandas as pd

vendas = {
    'cod_pedido': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'valor_venda': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'quantidade_de_itens': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
df_vendas = pd.DataFrame(vendas)
print(df_vendas)
#%%
df_vendas.head()
#%%
# Valor total de vendas
df_vendas['valor_venda'].sum()
#%%
# Quantidade total vendida
df_vendas['quantidade_de_itens'].sum()
#%%
# Quantidade de pedidos realizados
df_vendas['cod_pedido'].count()
#%%
# Valor de venda médio por pedido
df_vendas['valor_venda'].mean()
#%%
# Quantidade vendida média
df_vendas['quantidade_de_itens'].mean()
#%%
df_vendas.describe()
#%%
