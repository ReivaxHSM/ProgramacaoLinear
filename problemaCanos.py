# Problemas de Pesquisa Operacional
# Problema do canos
# Autor: Heráclito Xavier
# Data: 16/03/2024

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema dos canos", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Cano de 25 mm", 0)                           # Criação da variável de decisão
x2 = LpVariable("Cano de 40 mm", 0)                           # Criação da variável de decisão
x3 = LpVariable("Cano de 100 mm", 0)                          # Criação da variável de decisão

prob += x1 + 3*x2 + 5*x3                                      # Função objetivo
prob += 1/5*x1 + 1/4*x2 + 1/2*x3 <= 7000                      # Restrição de produção
prob += 1/5*x1 + 1/4*x2 + 1/2*x3 <= 9600                      # Restrição capacidade da extrusora quilos por dia
prob += x1 >= 1000                                            # Restrição de quantidade mínima de canos em metros por dia
prob += x2 >= 1000                                            # Restrição de quantidade mínima de canos em metros por dia
prob += x3 >= 1000                                            # Restrição de quantidade mínima de canos em metros por dia

prob.solve()                                                  # Resolução do problema
for v in prob.variables():                                    # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                            # Impressão das variáveis de decisão
print("Lucro máximo = ", value(prob.objective))               # Impressão do valor da função objetivo

