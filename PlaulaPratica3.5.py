# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.5 Empresa de chapa de aço
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Determine a produção que maximiza o lucro de uma empresa de chapas de aço inoxidável e de aço galvanizado que tem as seguintes informações 
sobre a fabricação desses itens: cada chapa de aço inoxidável requer uma hora de mão de obra e 5 quilos de aço e cada chapa de aço galvanizado 
requer uma hora de mão de obra e 4 quilos de aço. A empresa dispõe, semanalmente, de 2 toneladas de aço e de 500 horas de mão de obra. 
O lucro referente a cada chapa de aço inoxidável é R$ 12,00 e de cada chapa de aço galvanizado é R$ 10,00. Utilize a biblioteca PuLP 
do Python.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)     # Criação do problema de maximização
x1 = LpVariable("Chapa de aço inoxidável", 0)            # Criação da variável de decisão
x2 = LpVariable("Chapa de aço galvanizado", 0)           # Criação da variável de decisão

prob += 12*x1 + 10*x2                                    # Função objetivo
prob += 5*x1 + 4*x2 <= 2000                              # Restrição de aço
prob += x1 + x2 <= 500                                   # Restrição de mão de obra

prob.solve()                                             # Resolução do problema
for v in prob.variables():                               # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                       # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))          # Impressão do valor da função objetivo








