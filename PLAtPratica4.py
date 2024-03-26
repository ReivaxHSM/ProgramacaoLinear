# Problemas de Pesquisa Operacional
# Problema apliacada o transporte
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma indústria de brinquedos fabrica miniaturas de carros, arcos e motos. A matéria-prima utilizada é um tipo especial de plástico. Cada carro
utiliza 340 g de plástico. As quantidades de plático necessárias para a produção de cada barco e de cada moto são 420 g e 290 g, respectivamente..
Os lucros unitários referentes aos carros, barcos e motos são, respectivamente, R$ 22,00, R$ 18,00 e R$ 23,00. 
A produção máxima de carros é de 300 unidades e a produção mínima de motos é de 450 unidades. A quantidade de plástico disponível é de 3.300 kg.
A meta da indústria é obter o maior lucro possível e, para isso, pretende decidir quantas unidades de cada miniatura devem ser produzidas.
Determinando de C a quantidade de carros, B a quantidade de barcos e de M a quantidade de motos, formule o problema como um problema PL.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)           # Criação do problema de maximização
x1 = LpVariable("Carro", 0)                                    # Criação da variável de decisão
x2 = LpVariable("Barco", 0)                                    # Criação da variável de decisão
x3 = LpVariable("Moto", 0)                                     # Criação da variável de decisão

prob += 22*x1 + 18*x2 + 23*x3                                  # Função objetivo
prob += 0.340*x1 + 0.420*x2 + 0.290*x3 <= 3300                 # Restrição de produção
prob += x1 <= 300                                              # Restrição de quantidade máxima de carros
prob += x3 >= 450                                              # Restrição de quantidade mínima de motos

prob.solve()                                                   # Resolução do problema
for v in prob.variables():                                     # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                             # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                # Impressão do valor da função objetivo





