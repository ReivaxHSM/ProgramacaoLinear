# Problemas de Pesquisa Operacional
# Problema apliacada ao Comercio II
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Um açougue tem R$ 22.000,00 para comprar carne de frango, carne de gado e carne de porco. Para a compra da carne de frango, 
o custo por quilo é R$ 8,00. O custo referente a um quilo de carne de gado é R$ 17,00 e o custo referente a um quilo de carne 
de porco é R$ 15,00. O lucro associado à venda da carne de frango corresponde a R$ 10,00 por quilo, para a venda de um quilo 
de carne de gado o lucro é de R$ 19,00 e o lucro referente à venda de cada quilo de carne de porco é de R$ 16,00. 
Levando em consideração o histórico de vendas, a quantidade mínima a ser comprada de cada tipo de carne é de 500 quilos. 
O objetivo do açougue é maximizar o lucro referente à venda das carnes. Assim, quantos quilos de cada uma delas deverão 
ser comprados? Formule e resolva o problema como um problema de programação linear.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do açougue", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Carne de frango", 0)                          # Criação da variável de decisão
x2 = LpVariable("Carne de gado", 0)                            # Criação da variável de decisão
x3 = LpVariable("Carne de porco", 0)                           # Criação da variável de decisão

prob += 10*x1 + 19*x2 + 16*x3                                  # Função objetivo
prob += 8*x1 + 17*x2 + 15*x3 <= 22000                          # Restrição de orçamento
prob += x1 >= 500                                              # Restrição de quantidade mínima de carne de frango
prob += x2 >= 500                                              # Restrição de quantidade mínima de carne de gado
prob += x3 >= 500                                              # Restrição de quantidade mínima de carne de porco

prob.solve()                                                   # Resolução do problema
for v in prob.variables():                                     # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                             # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                # Impressão do valor da função objetivo
