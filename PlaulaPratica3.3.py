# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.3 Fábrica de artigos de Camping
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma empresa fabrica 2 artigos de camping: sacos de dormir e barracas. Cada saco de dormir requer 2 horas para cortar os tecidos, 
5 horas para costurar e 1 hora para impermeabilizar. Cada barraca requer 1 hora para cortar os tecidos, 5 horas para as costuras 
e 3 horas de impermeabilização. Dados os recursos limitados da empresa, ela dispõe de 14 horas para o corte, 
40 horas para a costura e 18 horas para a impermeabilização, por dia. A margem de lucro é de R$ 50,00 por saco de dormir 
e de R$ 30,00 por barraca. Resolva o problema utilizando a biblioteca PuLP do Python.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)     # Criação do problema de maximização
x1 = LpVariable("Saco de dormir", 0)                     # Criação da variável de decisão
x2 = LpVariable("Barraca", 0)                            # Criação da variável de decisão

prob += 50*x1 + 30*x2                                    # Função objetivo
prob += 2*x1 + 1*x2 <= 14                                # Restrição de corte
prob += 5*x1 + 5*x2 <= 40                                # Restrição de costura
prob += 1*x1 + 3*x2 <= 18                                # Restrição de impermeabilização

prob.solve()                                             # Resolução do problema
for v in prob.variables():                               # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                       # Impressão das variáveis de decisão    

print("Lucro máximo = ", value(prob.objective))          # Impressão do valor da função objetivo



