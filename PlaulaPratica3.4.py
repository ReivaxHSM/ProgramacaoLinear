# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.4 Industria de brinquedos
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma indústria de brinquedos fabrica miniaturas de aviões, barcos e helicópteros. A matéria-prima utilizada é um tipo especial de plástico. 
Cada avião utiliza 340 g de plástico. As quantidades de plástico necessárias para a produção de cada barco e de cada helicóptero são 420 g 
e 290 g, respectivamente. Os lucros unitários referentes aos aviões, barcos e helicópteros são, respectivamente, 
R$ 22,00, R$ 18,00 e R$ 23,00. A produção mínima de barcos é de 300 unidades e a produção mínima de aviões é de 450 unidades. 
A quantidade de plástico disponível é de 1.300 kg. A meta da indústria é obter o maior lucro possível e, para isso, pretende decidir 
quantas unidades de cada miniatura devem ser produzidas. Com base nessas informações, resolva por meio da biblioteca PuLP do Python 
o problema como um problema de PL.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)           # Criação do problema de maximização
x1 = LpVariable("Avião", 0)                                    # Criação da variável de decisão
x2 = LpVariable("Barco", 0)                                    # Criação da variável de decisão
x3 = LpVariable("Helicóptero", 0)                              # Criação da variável de decisão

prob += 22*x1 + 18*x2 + 23*x3                                  # Função objetivo
prob += 0.340*x1 + 0.420*x2 + 0.290*x3 <= 1300                       # Restrição de produção
prob += x2 >= 300                                               # Restrição de quantidade mínima de barcos
prob += x1 >= 450                                               # Restrição de quantidade mínima de aviões

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo






