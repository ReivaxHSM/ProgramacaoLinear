# Problemas de Pesquisa Operacional
# Problema apliacada a transportadora
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
O objetivo de uma transportadora é otimizar a utilização mensal de sua frota de caminhões obtendo assim o maior lucro total 
referente aos serviços prestados. Atualmente a transportadora conta com os seguintes veículos: 8 carretas, 16 caminhões médios 
e 12 caminhões pequenos. A empresa tem 32 motoristas e 61 ajudantes. Cada caminhão precisa de 1 motorista e o número de 
ajudantes depende do tipo de veículo: 1 ajudante para cada caminhão pequeno, 2 ajudantes para cada caminhão médio e 3 ajudantes 
para cada carreta. O lucro mensal referente a cada carreta corresponde a R$ 5.800,00. O lucro mensal relacionado a cada caminhão 
médio corresponde a R$ 3.300,00 e o lucro para cada caminhão pequeno é de R$ 2.800,00. A empresa deseja saber quantos caminhões 
de cada modelo irá utilizar mensalmente. Formule e resolva o problema como um problema de PL.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Carreta", 0)                                   # Criação da variável de decisão
x2 = LpVariable("Caminhao medio", 0)                            # Criação da variável de decisão
x3 = LpVariable("Caminhao pequeno", 0)                          # Criação da variável de decisão

prob += 5800*x1 + 3300*x2 + 2800*x3                             # Função objetivo
prob += x1 + x2 + x3 <= 32                                      # Restrição de quantidade de motoristas
prob += 3*x1 + 2*x2 + x3 <= 61                                  # Restrição de quantidade de ajudantes
prob += x1 <= 8                                                 # Restrição de quantidade máxima de carretas
prob += x2 <= 16                                                # Restrição de quantidade máxima de caminhões médios
prob += x3 <= 12                                                # Restrição de quantidade máxima de caminhões pequenos

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo


