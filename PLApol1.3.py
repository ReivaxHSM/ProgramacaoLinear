# Problemas de Pesquisa Operacional
# Problema apliacada o transporte
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma empresa de revenda de produtos da área de logística deseja adquirir uma certa quantidade de empilhadeiras e de porta pallets 
para completar seus estoques. A relação a seguir apresenta o custo referente à aquisição de cada um desses produtos, 
o lucro unitário e as quantidades mínimas e máximas a serem adquiridas: Empilhadeira: R$ 60.000,00 cada, lucro unitário de R$ 30.000,00,
mínimo de 10 e máximo de 50. Porta pallet: R$ 90,00 cada, lucro unitário de R$ 33,00, mínimo de 1000.
Sabendo que a empresa tem R$ 1.000.000,00 para investir na compra das empilhadeiras e dos porta pallets e que o objetivo é determinar 
a quantidade “e” de empilhadeiras e a quantidade “p” de porta pallets que fornece o maior lucro “L” possível, formule e resolva o problema
.'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do transporte", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Empilhadeira",0)                                 # Criação da variável de decisão
x2 = LpVariable("Porta pallet", 0)                                # Criação da variável de decisão

prob += 30000*x1 + 33*x2                                          # Função objetivo
prob += 60000*x1 + 90*x2 <= 1000000                               # Restrição de investimento
prob += x1 >= 10                                                  # Restrição de quantidade mínima de empilhadeiras
prob += x1 <= 50                                                  # Restrição de quantidade máxima de empilhadeiras
prob += x2 >= 1000                                                # Restrição de quantidade mínima de porta pallets

prob.solve()                                                      # Resolução do problema
for v in prob.variables():                                        # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                   # Impressão do valor da função objetivo


