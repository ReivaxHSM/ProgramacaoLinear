# Problemas de Pesquisa Operacional
# Problema apliacada ao Comercio I
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma revenda de equipamentos agrícolas deseja investir R$ 2.535.000,00 na compra de novos produtos para a loja. 
O setor de compras está analisando três tipos de equipamentos chamados de A, B e C. O equipamento A tem um custo 
unitário de R$ 9.200,00 e representa um lucro de R$ 3.400,00. O equipamento B custa R$ 6.700,00 com um lucro de R$ 2.900,00, 
e o equipamento C tem um custo unitário de R$ 17.000,00 com um lucro de R$ 4.300,00. O estoque mínimo de cada 
equipamento deverá ser de 20 unidades. A revenda precisa definir quantas unidades de cada equipamento serão
adquiridas de modo que o lucro total referente à venda dos equipamentos seja o maior possível. Formule e resolva o problema
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do revenda", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Equipamento A", 0)                            # Criação da variável de decisão
x2 = LpVariable("Equipamento B", 0)                            # Criação da variável de decisão
x3 = LpVariable("Equipamento C", 0)                            # Criação da variável de decisão

prob += 3400*x1 + 2900*x2 + 4300*x3                            # Função objetivo
prob += 9200*x1 + 6700*x2 + 17000*x3 <= 2535000                # Restrição de investimento
prob += x1 >= 20                                               # Restrição de quantidade mínima de equipamento A
prob += x2 >= 20                                               # Restrição de quantidade mínima de equipamento B
prob += x3 >= 20                                               # Restrição de quantidade mínima de equipamento C

prob.solve()                                                   # Resolução do problema
for v in prob.variables():                                     # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                             # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                # Impressão do valor da função objetivo
