# Problemas de Pesquisa Operacional
# Problema apliacada lojistica de transporte
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Um fornecedor de manetes esportivos para motocicletas recebeu pedidos de algumas lojas. O fornecedor dispõe de 2000 manetes. O custo de transporte
até a loja 1 é de R$ 3,00 por manete, até a loja 2 é de R$ 7,00 por manete e até a loja 3 é de R$ 5,00 por manete. A loja 1 tem uma demanda de 550
unidades, a loja 2 tem uma demanda de 1200 unidades e a loja 3 tem uma demanda de 720 unidades. Sabendo que o objetivo do fornecedor é minimizar 
o custo total de transporte, determine quantas unidades deverão ser transportadas do fornecedor para cada uma das lojas.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do transporte", LpMinimize)            # Criação do problema de minimização
x1 = LpVariable("Manetes para loja 1",0)                          # Criação da variável de decisão
x2 = LpVariable("Manetes para loja 2", 0)                         # Criação da variável de decisão
x3 = LpVariable("Manetes para loja 3", 0)                         # Criação da variável de decisão

prob += 3*x1 + 7*x2 + 5*x3                                        # Função objetivo
prob += x1 + x2 + x3 >= 2000                                      # Restrição de quantidade de manetes disponíveis é menor do que a demanda
prob += x1 <= 550                                                 # Restrição de quantidade máxima de manetes para a loja 1
prob += x2 <= 1200                                                # Restrição de quantidade máxima de manetes para a loja 2
prob += x3 <= 720                                                 # Restrição de quantidade máxima de manetes para a loja 3

prob.solve()                                                      # Resolução do problema
for v in prob.variables():                                        # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective))                   # Impressão do valor da função objetivo
