# Problemas de Pesquisa Operacional
# Problema apliacada o transporte
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma industria de brinquedos fabrica dois tipos de aeromodelos a controle remoto. Cada avião requer 200g de plástico e cada helicóptero 
requer 230g de plástico. A indústria tem, semanlamente, 600 quilos de plástico disponíveis. O lucro referente a cada avião é R$ 20,00 e
de cada helicóptero é R$ 18,00. A indústria deseja determinar quantas unidades de cada aeromodelo deve produzir para maximizar o lucro.
.'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)     # Criação do problema de maximização
x1 = LpVariable("Avião", 0)                               # Criação da variável de decisão
x2 = LpVariable("Helicóptero", 0)                         # Criação da variável de decisão

prob += 20*x1 + 18*x2                                     # Função objetivo
prob += 0.200*x1 + 0.230*x2 <= 600                        # Restrição de plástico

prob.solve()                                              # Resolução do problema
for v in prob.variables():                                # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                        # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))           # Impressão do valor da função objetivo



