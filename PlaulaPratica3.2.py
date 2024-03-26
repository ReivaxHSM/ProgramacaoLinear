# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.2 - distribuição de vitaminas e proteinas
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma nutricionista indicou para uma pessoa o uso de suplementos alimentares devido à necessita de vitaminas e de proteínas. 
Para esta pessoa, a necessidade adicional de vitaminas é de pelo menos 27 unidades por dia e de pelo menos 30 unidades por dia de proteínas. 
Uma unidade de medida do Suplemento A contém 3 unidades de vitaminas e 5 unidades de proteína. Uma unidade de medida do Suplemento B 
contém 6 unidades de vitaminas e 4 de proteínas. Uma unidade do Suplemento A custa R$ 4,00 e uma unidade do Suplemento B custa R$ 5,00. 
Sabendo que o objetivo é suprir as necessidades diárias de vitaminas e proteínas com o menor custo possível, resolva o problema por 
meio da biblioteca PuLP do Python.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da distribuição", LpMinimize)            # Criação do problema de minimização
x1 = LpVariable("Suplemento A", 0)                                   # Criação da variável de decisão
x2 = LpVariable("Suplemento B", 0)                                   # Criação da variável de decisão

prob += 4*x1 + 5*x2                                                 # Função objetivo
prob += 3*x1 + 6*x2 >= 27                                           # Restrição de quantidade mínima de vitaminas
prob += 5*x1 + 4*x2 >= 30                                           # Restrição de quantidade mínima de proteínas

prob.solve()                                                        # Resolução do problema
for v in prob.variables():                                          # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                  # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective))                     # Impressão do valor da função objetivo


