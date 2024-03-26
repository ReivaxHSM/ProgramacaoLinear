# Problemas de Pesquisa Operacional
# Problema Emissora de rádio
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma emissora de rádio tem 3 programas dedicados a diferentes estilos musicais. O programa A tem 60 minutos de duração onde 5 minutos e
são destinados aos comerciais e 55 minutos é destinado à MPB. O programa B tem 10 minutos de comerciais e 50 minutos de rock 
nacional. O programa C tem 15 minutos de comerciais e 45 minutos de rock internacional A direção da emissora tem como meta destinar
no máximo 30 horas semanais para música e pelo menos 100 minutos para comerciais. A audiência dos programas A, B e C é de 10.000, 
22.000 e 20.000 ouvintes, respectivamente. O objetivo da emissora é determinar quantas vezes cada um dos programas deve ser transmitido
semanalmente de modo que a audiência referente a esses programas seja o maior possível. Formule e resolva o problema como um problema de
programação Linear.
'''
# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da emissora", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Programa A", 0)                                 # Criação da variável de decisão
x2 = LpVariable("Programa B", 0)                                 # Criação da variável de decisão
x3 = LpVariable("Programa C", 0)                                 # Criação da variável de decisão

prob += 10000*x1 + 22000*x2 + 20000*x3                          # Função objetivo
prob += 55*x1 + 50*x2 + 45*x3 <= 30*60                          # Restrição de tempo de música
prob += 5*x1 + 10*x2 + 15*x3 >= 100                              # Restrição de tempo de comerciais

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão

print("Audiência máxima = ", value(prob.objective))             # Impressão do valor da função objetivo






