# Problemas de Pesquisa Operacional
# Problema Produtos
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma empresa pretende produzir dois produtos conhecidos como P1 e P2. Cada produto consome 240 gramas de matéria prima. A empresa tem, 
semanalmente, 12000 quilos de matéria prima. O lucro referente ao produto P1 é R$ 23,00 e o lucro referente ao produto P2 é R$ 32,00.
Determine qual é a produção que maximiza o lucro.
'''
# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)     # Criação do problema de maximização
x1 = LpVariable("Produto P1", 0)                         # Criação da variável de decisão
x2 = LpVariable("Produto P2", 0)                         # Criação da variável de decisão

prob += 23*x1 + 32*x2                                    # Função objetivo
prob += 0.240*x1 + 0.240*x2 <= 12000                     # Restrição de matéria prima

prob.solve()                                             # Resolução do problema
for v in prob.variables():                               # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                       # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))          # Impressão do valor da função objetivo





