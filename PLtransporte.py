# Problemas de Pesquisa Operacional
# Problema apliacada o transporte
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma empresa da área de logística precisa adquirir uma certa quantidade de empilhadeiras e de porta pallets. 
A seguir são apresentadas algumas informações importantes: o custo referente à aquisição de cada um destes itens 
e as quantidades mínimas e máximas a serem adquiridas. Empilhadeira: R$ 70.000,00 cada, mínimo de 15 e máximo de 50.
Porta pallet: R$ 1200,00 cada, mínimo de 400 e máximo de 40.Sabendo que a empresa tem R$ 1.600.000,00 para investir 
na compra das empilhadeiras e dos porta pallets e que deseja minimizar o custo total referente à aquisição destes itens, 
determine quantas empilhadeiras e quantos porta pallets deverá comprar.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do transporte", LpMinimize)            # Criação do problema de minimização
x1 = LpVariable("Empilhadeira",0)                                 # Criação da variável de decisão
x2 = LpVariable("Porta pallet", 0)                                # Criação da variável de decisão

prob += 70000*x1 + 1200*x2                                        # Função objetivo
prob += 70000*x1 + 1200*x2 <= 1600000                             # Restrição de investimento
prob += x1 >= 15                                                  # Restrição de quantidade mínima de empilhadeiras
prob += x1 <= 50                                                  # Restrição de quantidade máxima de empilhadeiras
prob += x2 >= 400                                                 # Restrição de quantidade mínima de porta pallets

prob.solve()                                                      # Resolução do problema
for v in prob.variables():                                        # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective))                   # Impressão do valor da função objetivo


