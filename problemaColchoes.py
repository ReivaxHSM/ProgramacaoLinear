# Problemas de Pesquisa Operacional
# Problema do colchões
# Autor: Heráclito Xavier
# Data: 16/03/2024

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema dos colchões", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Colchão de Solteiro", 0)                        # Criação da variável de decisão
x2 = LpVariable("Colchão de Casal", 0)                           # Criação da variável de decisão
x3 = LpVariable("Colchão Queen", 0)                              # Criação da variável de decisão
x4 = LpVariable("Colchão King", 0)                               # Criação da variável de decisão

prob += 320*x1 + 370*x2 + 400*x3 + 420*x4                        # Função objetivo
prob += 300*x1 + 550*x2 + 980*x3 + 1200*x4 <= 110000             # Restrição de produção
prob += x1 >= 50                                                 # Restrição de quantidade mínima de colchões
prob += x2 >= 100                                                # Restrição de quantidade mínima de colchões
prob += x3 >= 20                                                 # Restrição de quantidade mínima de colchões
prob += x4 >= 10                                                 # Restrição de quantidade mínima de colchões

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão
print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo


