# Problemas de Pesquisa Operacional
# Problema Locadora
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma locadora de automóveis, devido ao aumento da demanda, precisa adquirir novos automóveis. Atualmente há três tipos de veículos à 
disposição dos clientes: automóveis populares, veículos de luxo e esportivos utilitários. A locadora tem R$ 1.700.000,00 destinados 
à compra desses automóveis. A demanda mínima de cada veículo é de 8 automóveis populares, 4 veículos de luxo e 3 esportivos utilitários. 
O custo desses automóveis é de R$ 23.000,00 para cada automóvel popular, R$ 64.000,00 para cada veículo de luxo e R$ 77.000,00 
para cada esportivo utilitário. Os lucros diários associados a cada um desses automóveis são, respectivamente, R$ 110,00, R$ 180,00 
e R$ 200,00. Sabe-se que o objetivo da locadora é determinar quantos automóveis de cada tipo devem ser adquiridos de modo que o lucro da 
locadora seja o maior possível. Considerando L = lucro, AP = quantidade de automóveis populares, VL = quantidade de veículos de luxo e 
EU = quantidade de esportivos utilitários, resolva o problema como um problema de programação Linear. 
'''
# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da locadora", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Automóvel popular", 0)                         # Criação da variável de decisão
x2 = LpVariable("Veículo de luxo", 0)                           # Criação da variável de decisão
x3 = LpVariable("Esportivo utilitário", 0)                      # Criação da variável de decisão

prob += 110*x1 + 180*x2 + 200*x3                                # Função objetivo
prob += 23000*x1 + 64000*x2 + 77000*x3 <= 1700000               # Restrição de investimento
prob += x1 >= 8                                                # Restrição de quantidade mínima de automóveis populares
prob += x2 >= 4                                                # Restrição de quantidade mínima de veículos de luxo
prob += x3 >= 3                                                # Restrição de quantidade mínima de esportivos utilitários

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo





