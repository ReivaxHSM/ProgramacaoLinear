# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.1 - Fábrica de equipamentos.
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma fábrica de equipamentos para gráficas produz os modelos A, B e C, que geram lucros unitários de R$ 12.000,00, 
R$ 22.000,00 e $ 15.000,00, respectivamente. A produção mínima mensal é de 10 unidades do modelo A, 30 unidades 
do modelo B e 20 unidades do modelo C. Uma unidade do modelo A necessita de 4 horas para fabricar, 
5 horas para montar e 1 hora para testar. Uma unidade do modelo B necessita de 3 horas para fabricar, 
5 horas para montar e 2 horas para testar. Uma unidade do modelo C necessita de 3 horas para fabricar, 4 horas para montar 
e 1 hora para testar. A fábrica tem à disposição 400 horas de tempo de fabricação, 700 horas de montagem e 150 horas 
de testes de qualidade. Resolva o problema de programação de produção como um problema de programação linear.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Modelo A", 0)                                    # Criação da variável de decisão
x2 = LpVariable("Modelo B", 0)                                      # Criação da variável de decisão
x3 = LpVariable("Modelo C", 0)                                      # Criação da variável de decisão

prob += 12000*x1 + 22000*x2 + 15000*x3                            # Função objetivo
prob += 4*x1 + 3*x2 + 3*x3 <= 400                                           # Restrição de fabricação
prob += 5*x1 + 5*x2 + 4*x3 <= 700                                           # Restrição de montagem
prob += 1*x1 + 2*x2 + 1*x3 <= 150                                           # Restrição de testes de qualidade
prob += x1 >= 10                                               # Restrição de quantidade mínima de modelo A
prob += x2 >= 30                                               # Restrição de quantidade mínima de modelo B
prob += x3 >= 20                                               # Restrição de quantidade mínima de modelo C

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo
