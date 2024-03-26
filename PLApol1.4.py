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

prob += 120*x1 + 97*x2                          # Função objetivo
prob += 10*x1 + 15*x2 <= 300                    # Restrição 1
prob += x2 <= 10                                # Restrição 2

prob.solve()                                    # Resolução do problema
for v in prob.variables():                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)              # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective)) # Impressão do valor da função objetivo



