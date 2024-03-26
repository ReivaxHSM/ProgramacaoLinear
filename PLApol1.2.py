# Problemas de Pesquisa Operacional
# Problema de PL APOL 
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Resolva o seguinte problema de PL
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema de PL", LpMaximize)  # Criação do problema de minimização
x1 = LpVariable("x1",0)                         # Criação da variável de decisão  
x2 = LpVariable("x2", 0)                        # Criação da variável de decisão

prob += 70*x1 + 40*x2                           # Função objetivo
prob += 33*x1 + 14*x2 <= 2200                   # Restrição 1
prob += 4*x1 + 17*x2 <= 1344                    # Restrição 2

prob.solve()                                    # Resolução do problema
for v in prob.variables():                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)              # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective)) # Impressão do valor da função objetivo



