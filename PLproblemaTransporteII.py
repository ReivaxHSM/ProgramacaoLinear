# Problemas de Pesquisa Operacional
# Problema apliacada lojistica de transporte II
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
O problema de transporte de uma fábrica de chapas de MDF cru de 15 mm consiste em determinar quantas unidades serão transportadas 
de cada depósito para cada revenda. No Depósito 1 há 2000 chapas e no Depósito 2 o estoque é de 4000 chapas. A Revenda 1 precisa 
de 1400 chapas, a Revenda 2 tem uma demanda de 3000 chapas e a Revenda 3 necessita de 1100 chapas
Os custos unitários de transportes são o seguinte: do Depósito 1 para a Revenda 1 é de R$ 10,00, do Depósito 1 para a Revenda 2 é de R$ 12,00,
do Depósito 1 para a Revenda 3 é de R$ 9,00, do Depósito 2 para a Revenda 1 é de R$ 15,00, do Depósito 2 para a Revenda 2 é de R$ 11,00 e
do Depósito 2 para a Revenda 3 é de R$ 17,00. Sabendo que o objetivo da fábrica é determinar quantas unidades serão transportadas de cada 
depósito para cada revenda a fim de minimizar o custo total, formule e resolva o problema como um problema de programação linear.
Observação: Neste porblema a demanda é menor do que a oferta
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do transporte", LpMinimize)            # Criação do problema de minimização
x11 = LpVariable("Chapas do Depósito 1 para a Revenda 1",0)       # Criação da variável de decisão
x12 = LpVariable("Chapas do Depósito 1 para a Revenda 2", 0)      # Criação da variável de decisão
x13 = LpVariable("Chapas do Depósito 1 para a Revenda 3", 0)      # Criação da variável de decisão
x21 = LpVariable("Chapas do Depósito 2 para a Revenda 1", 0)      # Criação da variável de decisão
x22 = LpVariable("Chapas do Depósito 2 para a Revenda 2", 0)      # Criação da variável de decisão
x23 = LpVariable("Chapas do Depósito 2 para a Revenda 3", 0)      # Criação da variável de decisão

prob += 10*x11 + 12*x12 + 9*x13 + 15*x21 + 11*x22 + 17*x23        # Função objetivo
prob += x11 + x12 + x13 <= 2000                                   # Restrição de quantidade de chapas disponíveis no Depósito 1
prob += x21 + x22 + x23 <= 4000                                   # Restrição de quantidade de chapas disponíveis no Depósito 2
prob += x11 + x21 >= 1400                                         # Restrição de quantidade de chapas para a Revenda 1
prob += x12 + x22 >= 3000                                         # Restrição de quantidade de chapas para a Revenda 2
prob += x13 + x23 >= 1100                                         # Restrição de quantidade de chapas para a Revenda 3

prob.solve()                                                      # Resolução do problema
for v in prob.variables():                                        # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective))                   # Impressão do valor da função objetivo