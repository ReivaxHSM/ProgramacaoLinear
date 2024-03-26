# Problemas de Pesquisa Operacional
# Problema das toalhas
# Autor: Heráclito Xavier
# Data: 16/03/2024

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema das toalhas", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Toalha de Banho", 0)                           # Criação da variável de decisão
x2 = LpVariable("Toalha de Rosto", 0)                           # Criação da variável de decisão

prob += 15*x1 + 7*x2                                            # Função objetivo
prob += 0.4*x1 + 0.18*x2 <= 5000                                # Restrição de tecido
prob += x2 <= 20000                                             # Restrição de quantidade de toalhas de rosto

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão
print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo
