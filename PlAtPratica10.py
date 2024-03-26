# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.9 Designação de local
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Resolva o seguinte problema de designação onde o objetivo é minimizar o custo total de instalação das máquinas nos respectivos locais
	
		Local 1 	Local 2		Local 3
Máquina 1	3000		2800		3300
Máquina 2	3840		2210		3500
Máquina 3	2000		2500		2700
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema de designação", LpMinimize)                                        # Criação do problema de minimização
x11 = LpVariable("Máquina 1 no local 1", 0)                                                    # Criação da variável de decisão
x12 = LpVariable("Máquina 1 no local 2", 0)                                                    # Criação da variável de decisão
x13 = LpVariable("Máquina 1 no local 3", 0)                                                    # Criação da variável de decisão
x21 = LpVariable("Máquina 2 no local 1", 0)                                                    # Criação da variável de decisão
x22 = LpVariable("Máquina 2 no local 2", 0)                                                    # Criação da variável de decisão
x23 = LpVariable("Máquina 2 no local 3", 0)                                                    # Criação da variável de decisão
x31 = LpVariable("Máquina 3 no local 1", 0)                                                    # Criação da variável de decisão
x32 = LpVariable("Máquina 3 no local 2", 0)                                                    # Criação da variável de decisão
x33 = LpVariable("Máquina 3 no local 3", 0)                                                    # Criação da variável de decisão

prob += 3000*x11 + 2800*x12 + 3300*x13 + 3840*x21 + 2210*x22 + 3500*x23 + 2000*x31 + 2500*x32 + 2700*x33        # Função objetivo
prob += x11 + x12 + x13 == 1                                                                  # Restrição de designação da máquina 1
prob += x21 + x22 + x23 == 1                                                                  # Restrição de designação da máquina 2
prob += x31 + x32 + x33 == 1                                                                  # Restrição de designação da máquina 3
prob += x11 + x21 + x31 == 1                                                                  # Restrição de designação do local 1
prob += x12 + x22 + x32 == 1                                                                  # Restrição de designação do local 2
prob += x13 + x23 + x33 == 1                                                                  # Restrição de designação do local 3

prob.solve()                                                                                 # Resolução do problema
for v in prob.variables():                                                                   # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                                           # Impressão das variáveis de decisão

print("Custo total de instalação = ", value(prob.objective))                                  # Impressão do valor da função objetivo












