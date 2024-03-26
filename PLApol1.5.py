# Problemas de Pesquisa Operacional
# Problema Aula Pratica Apol 1.5 Loja de informática
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Um comerciante possui uma loja de informática e precisa adquirir alguns produtos. A relação a seguir apresenta 
informações importantes a respeito de cada produto a ser adquirido: Laptop, preço de custo R$ 470,00; Lucro unitário R$ 200,00; 
quantidade mínima 10 unidades;Tablet, preço de custo R$ 190,00; Lucro unitário R$ 225,00; quantidade mínima 20 unidades; 
quantidade máxima 35 unidades; Mouse, preço de custo R$ 9,00; Lucro unitário R$ 10,00. Sabendo que o capital disponível 
para a aquisição desses produtos é de R$ 25.000,00 determine quantas unidades devem ser compradas de cada produto 
de modo que o lucro referente à posterior venda desses produtos seja o maior possível.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da loja de informática", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Laptop",0)                                                # Criação da variável de decisão
x2 = LpVariable("Tablet", 0)                                               # Criação da variável de decisão
x3 = LpVariable("Mouse", 0)                                                # Criação da variável de decisão

prob += 200*x1 + 225*x2 + 10*x3                                           # Função objetivo
prob += 470*x1 + 190*x2 + 9*x3 <= 25000                                    # Restrição de investimento
prob += x1 >= 10                                                           # Restrição de quantidade mínima de laptops
prob += x2 >= 20                                                           # Restrição de quantidade mínima de tablets
prob += x2 <= 35                                                           # Restrição de quantidade máxima de tablets

prob.solve()                                                               # Resolução do problema
for v in prob.variables():                                                 # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                         # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                            # Impressão do valor da função objetivo








