# Problemas de Pesquisa Operacional
# Problema de Designação
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma empresa de medicamentos possui representantes que atuam em três regiões. O potencial de venda em porcentagem dos representantes em
cada região é a seguinte: representante 1 para região 1, 85%; representante 1 para região 2, 97%; representante 1 para região 3, 82%;
representante 2 para região 1, 79%; representante 2 para região 2, 83%; representante 2 para região 3, 74%; representante 3 para região 1, 81%;
representante 3 para região 2, 85%; representante 3 para região 3, 89%. Qual deve ser a designação dos representantes para as regiões 
de modo que o potencial total de venda da empresa seja o maior possível?

'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema de designação", LpMaximize)                                        # Criação do problema de maximização
x11 = LpVariable("Representante 1 para região 1", 0)                                          # Criação da variável de decisão
x12 = LpVariable("Representante 1 para região 2", 0)                                          # Criação da variável de decisão
x13 = LpVariable("Representante 1 para região 3", 0)                                          # Criação da variável de decisão
x21 = LpVariable("Representante 2 para região 1", 0)                                          # Criação da variável de decisão
x22 = LpVariable("Representante 2 para região 2", 0)                                          # Criação da variável de decisão
x23 = LpVariable("Representante 2 para região 3", 0)                                          # Criação da variável de decisão
x31 = LpVariable("Representante 3 para região 1", 0)                                          # Criação da variável de decisão
x32 = LpVariable("Representante 3 para região 2", 0)                                          # Criação da variável de decisão
x33 = LpVariable("Representante 3 para região 3", 0)                                          # Criação da variável de decisão

prob += 85*x11 + 97*x12 + 82*x13 + 79*x21 + 83*x22 + 74*x23 + 81*x31 + 85*x32 + 89*x33        # Função objetivo
prob += x11 + x12 + x13 == 1                                                                  # Restrição de designação do representante 1
prob += x21 + x22 + x23 == 1                                                                  # Restrição de designação do representante 2
prob += x31 + x32 + x33 == 1                                                                  # Restrição de designação do representante 3
prob += x11 + x21 + x31 == 1                                                                  # Restrição de designação da região 1
prob += x12 + x22 + x32 == 1                                                                  # Restrição de designação da região 2
prob += x13 + x23 + x33 == 1                                                                  # Restrição de designação da região 3

prob.solve()                                                                                 # Resolução do problema
for v in prob.variables():                                                                   # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                                           # Impressão das variáveis de decisão

print("Potencial de venda total = ", value(prob.objective))                                  # Impressão do valor da função objetivo

