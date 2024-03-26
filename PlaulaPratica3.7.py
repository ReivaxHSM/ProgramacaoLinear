# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.7 DESIGNAÇÃO DE MÁQUINAS
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Problemas de designação podem ser resolvidos como problemas de transporte. Um problema de designação consiste basicamente em um problema 
onde cada origem tem apenas uma unidade disponível e cada destino necessita também de apenas uma unidade. Uma empresa precisa realizar 
a instalação de cinco máquinas em cinco locais diferentes. A tabela a seguir apresenta os custos de instalação de cada máquina nos 
respectivos lugares.Os custos de instação de cada máquina relacionados aos seus locais são os seguintes: maquina 1 no local 1: R$ 300,00;
maquina 1 no local 2: R$ 900,00; maquina 1 no local 3: R$ 100,00; maquina 1 no local 4: R$ 450,00; maquina 2 no local 1: R$ 840,00;
maquina 2 no local 2: R$ 210,00; maquina 2 no local 3: R$ 900,00; maquina 2 no local 4: R$ 670,00; maquina 3 no local 1: R$ 1000,00;
maquina 3 no local 2: R$ 460,00; maquina 3 no local 3: R$ 700,00; maquina 3 no local 4: R$ 550,00; maquina 4 no local 1: R$ 790,00;
maquina 4 no local 2: R$ 640,00; maquina 4 no local 3: R$ 800,00; maquina 4 no local 4: R$ 900,00.
Determine em qual local cada máquina deve ser instalada para minimizar o custo total de instalação.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do transporte", LpMinimize)            # Criação do problema de minimização
x11 = LpVariable("Maquina 1 no local 1",0)                        # Criação da variável de decisão
x12 = LpVariable("Maquina 1 no local 2", 0)                       # Criação da variável de decisão
x13 = LpVariable("Maquina 1 no local 3", 0)                       # Criação da variável de decisão
x14 = LpVariable("Maquina 1 no local 4", 0)                       # Criação da variável de decisão
x21 = LpVariable("Maquina 2 no local 1", 0)                       # Criação da variável de decisão
x22 = LpVariable("Maquina 2 no local 2", 0)                       # Criação da variável de decisão
x23 = LpVariable("Maquina 2 no local 3", 0)                       # Criação da variável de decisão
x24 = LpVariable("Maquina 2 no local 4", 0)                       # Criação da variável de decisão
x31 = LpVariable("Maquina 3 no local 1", 0)                       # Criação da variável de decisão
x32 = LpVariable("Maquina 3 no local 2", 0)                       # Criação da variável de decisão
x33 = LpVariable("Maquina 3 no local 3", 0)                       # Criação da variável de decisão
x34 = LpVariable("Maquina 3 no local 4", 0)                       # Criação da variável de decisão
x41 = LpVariable("Maquina 4 no local 1", 0)                       # Criação da variável de decisão
x42 = LpVariable("Maquina 4 no local 2", 0)                       # Criação da variável de decisão
x43 = LpVariable("Maquina 4 no local 3", 0)                       # Criação da variável de decisão
x44 = LpVariable("Maquina 4 no local 4", 0)                       # Criação da variável de decisão

prob += 300*x11 + 900*x12 + 100*x13 + 450*x14 + 840*x21 + 210*x22 + 900*x23 + 670*x24 + 1000*x31 + 460*x32 + 700*x33 + 550*x34 + 790*x41 + 640*x42 + 800*x43 + 900*x44        # Função objetivo
prob += x11 + x12 + x13 + x14 == 1                                # Restrição de designação da máquina 1
prob += x21 + x22 + x23 + x24 == 1                                # Restrição de designação da máquina 2
prob += x31 + x32 + x33 + x34 == 1                                # Restrição de designação da máquina 3
prob += x41 + x42 + x43 + x44 == 1                                # Restrição de designação da máquina 4
prob += x11 + x21 + x31 + x41 == 1                                # Restrição de designação do local 1
prob += x12 + x22 + x32 + x42 == 1                                # Restrição de designação do local 2
prob += x13 + x23 + x33 + x43 == 1                                # Restrição de designação do local 3
prob += x14 + x24 + x34 + x44 == 1                                # Restrição de designação do local 4

prob.solve()                                                      # Resolução do problema
for v in prob.variables():                                        # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective))                   # Impressão do valor da função objetivo












