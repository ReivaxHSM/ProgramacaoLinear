# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.9 Designação de local
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Resolva o seguinte problema de designação onde o objetivo é minimizar o custo total de instalação das máquinas nos respectivos locais
	
		    Local 1 	Local 2		Local 3
Máquina 1	50		    75		    67
Máquina 2	80		    77		    70
Máquina 3	68  		75		    77
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema de designação", LpMinimize)                                        # Criação do problema de minimização
x11 = LpVariable("Máquina 1 no local 1", 0)                                                   # Criação da variável de decisão
x12 = LpVariable("Máquina 1 no local 2", 0)                                                   # Criação da variável de decisão
x13 = LpVariable("Máquina 1 no local 3", 0)                                                   # Criação da variável de decisão
x21 = LpVariable("Máquina 2 no local 1", 0)                                                   # Criação da variável de decisão
x22 = LpVariable("Máquina 2 no local 2", 0)                                                   # Criação da variável de decisão
x23 = LpVariable("Máquina 2 no local 3", 0)                                                   # Criação da variável de decisão
x31 = LpVariable("Máquina 3 no local 1", 0)                                                   # Criação da variável de decisão
x32 = LpVariable("Máquina 3 no local 2", 0)                                                   # Criação da variável de decisão
x33 = LpVariable("Máquina 3 no local 3", 0)                                                   # Criação da variável de decisão

prob += 50*x11 + 75*x12 + 67*x13 + 80*x21 + 77*x22 + 70*x23 + 68*x31 + 75*x32 + 77*x33        # Função objetivo
prob += x11 + x12 + x13 == 1                                                                  # Restrição de designação da máquina 1
prob += x21 + x22 + x23 == 1                                                                  # Restrição de designação da máquina 2
prob += x31 + x32 + x33 == 1                                                                  # Restrição de designação da máquina 3
prob += x11 + x21 + x31 == 1                                                                  # Restrição de designação do local 1
prob += x12 + x22 + x32 == 1                                                                  # Restrição de designação do local 2  
prob += x13 + x23 + x33 == 1                                                                  # Restrição de designação do local 3

prob.solve()                                                                                  # Resolução do problema
for v in prob.variables():                                                                    # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                                            # Impressão das variáveis de decisão

print("Custo total de instalação = ", value(prob.objective))                                  # Impressão do valor da função objetivo













