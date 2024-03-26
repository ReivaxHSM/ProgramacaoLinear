# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.9 Designação de vendedores
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
A tabela a seguir apresenta o potencial de venda, em porcentagem, dos vendedores de uma empresa em três regiões:
		Região 1   	Região 2 	Região 3
Vendedor 1	89%		93%		92%
Vendedor 2	78%		67%		74%
Vendedor 3	76%		85%		79%
Qual deve ser a designação destes vendedores para as regiões consideradas de modo que o potencial total de vendas seja o maior possível.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema de designação", LpMaximize)                                        # Criação do problema de maximização
x11 = LpVariable("Vendedor 1 para região 1", 0)                                               # Criação da variável de decisão
x12 = LpVariable("Vendedor 1 para região 2", 0)                                               # Criação da variável de decisão
x13 = LpVariable("Vendedor 1 para região 3", 0)                                               # Criação da variável de decisão
x21 = LpVariable("Vendedor 2 para região 1", 0)                                               # Criação da variável de decisão
x22 = LpVariable("Vendedor 2 para região 2", 0)                                               # Criação da variável de decisão
x23 = LpVariable("Vendedor 2 para região 3", 0)                                               # Criação da variável de decisão
x31 = LpVariable("Vendedor 3 para região 1", 0)                                               # Criação da variável de decisão
x32 = LpVariable("Vendedor 3 para região 2", 0)                                               # Criação da variável de decisão
x33 = LpVariable("Vendedor 3 para região 3", 0)                                               # Criação da variável de decisão

prob += 89*x11 + 93*x12 + 92*x13 + 78*x21 + 67*x22 + 74*x23 + 76*x31 + 85*x32 + 79*x33        # Função objetivo
prob += x11 + x12 + x13 == 1                                                                  # Restrição de designação do vendedor 1
prob += x21 + x22 + x23 == 1                                                                  # Restrição de designação do vendedor 2
prob += x31 + x32 + x33 == 1                                                                  # Restrição de designação do vendedor 3
prob += x11 + x21 + x31 == 1                                                                  # Restrição de designação da região 1
prob += x12 + x22 + x32 == 1                                                                  # Restrição de designação da região 2
prob += x13 + x23 + x33 == 1                                                                  # Restrição de designação da região 3

prob.solve()                                                                                 # Resolução do problema
for v in prob.variables():                                                                   # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                                           # Impressão das variáveis de decisão

print("Potencial de venda total = ", value(prob.objective))                                  # Impressão do valor da função objetivo











