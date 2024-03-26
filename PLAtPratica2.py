# Problemas de Pesquisa Operacional
# Problema apliacada Revenda de Motos
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma refenda de motocicletas deseja investir R$ 1.200.000,00 na aquisição de novos produtos para a loja. Estão em análise 3 tipos de veículos:
A, B e C. A motocicleta A tem um custo unitário de R$ 11.300,00 e representa um lucro de R$ 8.500,00. A motocicleta B custa R$ 13.000,00 com 
um lucro de R$ 7.200,00, e a motocicleta C tem um custo unitário de R$ 22.000,00 com um lucro de R$ 11.300,00. O estoque mínimo de cada 
motocicleta deverá ser de 10 unidades. A revenda precisa definir quantas unidades de cada motocicleta serão adquiridas de modo que o lucro
referente a venda dessas motos seja o maior possível. Formule e resolva o problema
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da revenda", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Motocicleta A", 0)                            # Criação da variável de decisão
x2 = LpVariable("Motocicleta B", 0)                            # Criação da variável de decisão
x3 = LpVariable("Motocicleta C", 0)                            # Criação da variável de decisão

prob += 8500*x1 + 7200*x2 + 11300*x3                           # Função objetivo
prob += 11300*x1 + 13000*x2 + 22000*x3 <= 1200000              # Restrição de investimento
prob += x1 >= 10                                               # Restrição de quantidade mínima de motocicleta A
prob += x2 >= 10                                               # Restrição de quantidade mínima de motocicleta B
prob += x3 >= 10                                               # Restrição de quantidade mínima de motocicleta C

prob.solve()                                                   # Resolução do problema
for v in prob.variables():                                     # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                             # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                # Impressão do valor da função objetivo






