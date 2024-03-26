# Problemas de Pesquisa Operacional
# Problema apliacada a transportadora
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma transportadora possui uma frota de caminhões e deseja otimizar a utilização mensal deles de tal maneira que o lucro total 
referente aos serviços prestados seja maximizado. A transportadora possui os segintes veculos: 7 carretas, 12 caminhões médios
e 8 caminhões pequenos. Devido às atuais demandas, no quadro de funcionários há 20 motoristas e 48 ajudantes. Cada veículo, para
trafegar, precisa de 1 motorista. O número de ajudantes depende do tipo de veículo: 1 para cada caminhão pequeno, 2 para cada
caminhão médio e 3 para cada carreta. O lucro mensal referente a cada carreta é de R$ 3.400,00. O lucro mensal relacionado a cada
caminhão médio é de R$ 2.200,00 e o lucro para cada caminhão pequeno é de R$ 1.500,00. A empresa deseja saber quantos caminhões 
de cada modelo irá utilizar mensalmente. Formule e resolva o problema como um problema de PL.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Carreta", 0)                                   # Criação da variável de decisão
x2 = LpVariable("Caminhao medio", 0)                            # Criação da variável de decisão
x3 = LpVariable("Caminhao pequeno", 0)                          # Criação da variável de decisão

prob += 3400*x1 + 2200*x2 + 1500*x3                             # Função objetivo
prob += x1 + x2 + x3 <= 20                                      # Restrição de quantidade de motoristas
prob += 3*x1 + 2*x2 + x3 <= 48                                  # Restrição de quantidade de ajudantes
prob += x1 <= 7                                                 # Restrição de quantidade máxima de carretas
prob += x2 <= 12                                                # Restrição de quantidade máxima de caminhões médios
prob += x3 <= 8                                                 # Restrição de quantidade máxima de caminhões pequenos

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo




