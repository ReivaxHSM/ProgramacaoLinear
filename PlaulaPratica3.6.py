# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.6 Empresa Distribuidora 
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma empresa tem três depósitos com 350, 400 e 320 unidades, respectivamente, de um certo produto. Estes produtos precisam ser enviados 
a quatro lojas cujas demandas são, respectivamente, 210, 180, 340 e 300 unidades. Os custos de distrbuição são os seguintes: Depósito 1
para loja 1: R$ 103,00 por unidade; Depósito 1 para loja 2: R$ 97,00 por unidade; Depósito 1 para loja 3: R$ 111,00 por unidade; Depósito 1
para loja 4: R$ 107,00 por unidade; Depósito 2 para loja 1: R$ 122,00 por unidade; Depósito 2 para loja 2: R$ 117,00 por unidade; Depósito 2
para loja 3: R$ 130,00 por unidade; Depósito 2 para loja 4: R$ 121,00 por unidade; Depósito 3 para loja 1: R$ 98,00 por unidade; Depósito 3
para loja 2: R$ 100,00 por unidade; Depósito 3 para loja 3: R$ 85,00 por unidade; Depósito 3 para loja 4: R$ 110,00 por unidade. 
Determine quantas unidades devem ser transportadas de cada origem para cada destino de modo que o custo total de transporte 
seja o menor possível.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do transporte", LpMinimize)            # Criação do problema de minimização
x11 = LpVariable("Depósito 1 para loja 1",0)                      # Criação da variável de decisão
x12 = LpVariable("Depósito 1 para loja 2", 0)                     # Criação da variável de decisão
x13 = LpVariable("Depósito 1 para loja 3", 0)                     # Criação da variável de decisão
x14 = LpVariable("Depósito 1 para loja 4", 0)                     # Criação da variável de decisão
x21 = LpVariable("Depósito 2 para loja 1", 0)                     # Criação da variável de decisão
x22 = LpVariable("Depósito 2 para loja 2", 0)                     # Criação da variável de decisão
x23 = LpVariable("Depósito 2 para loja 3", 0)                     # Criação da variável de decisão
x24 = LpVariable("Depósito 2 para loja 4", 0)                     # Criação da variável de decisão
x31 = LpVariable("Depósito 3 para loja 1", 0)                     # Criação da variável de decisão
x32 = LpVariable("Depósito 3 para loja 2", 0)                     # Criação da variável de decisão
x33 = LpVariable("Depósito 3 para loja 3", 0)                     # Criação da variável de decisão
x34 = LpVariable("Depósito 3 para loja 4", 0)                     # Criação da variável de decisão

prob += 103*x11 + 97*x12 + 111*x13 + 107*x14 + 122*x21 + 117*x22 + 130*x23 + 121*x24 + 98*x31 + 100*x32 + 85*x33 + 110*x34        # Função objetivo
prob += x11 + x12 + x13 + x14 <= 350                              # Restrição de quantidade de produtos disponíveis no Depósito 1
prob += x21 + x22 + x23 + x24 <= 400                              # Restrição de quantidade de produtos disponíveis no Depósito 2
prob += x31 + x32 + x33 + x34 <= 320                              # Restrição de quantidade de produtos disponíveis no Depósito 3
prob += x11 + x21 + x31 >= 210                                    # Restrição de quantidade de produtos para a Loja 1
prob += x12 + x22 + x32 >= 180                                    # Restrição de quantidade de produtos para a Loja 2
prob += x13 + x23 + x33 >= 340                                    # Restrição de quantidade de produtos para a Loja 3
prob += x14 + x24 + x34 >= 300                                    # Restrição de quantidade de produtos para a Loja 4

prob.solve()                                                      # Resolução do problema
for v in prob.variables():                                        # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective))                   # Impressão do valor da função objetivo










