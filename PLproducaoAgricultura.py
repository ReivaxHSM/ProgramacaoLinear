# Problemas de Pesquisa Operacional
# Problema do canos
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Um agricultor produz feijão e soja e pretende decidir quantos hectares irá dedicar a cada cultura de modo a maximizar 
o lucro total. Para cada hectare de feijão irrigado, o lucro líquido estimado é de R$ 1.600,00, e para cada hectare 
de soja irrigada, estima-se que o lucro seja de R$ 2.500,00. A quantidade máxima de terra disponível é de 80 hectares. 
Contratos assinados exigem que a produção mínima de feijão seja de 20 hectares e a produção mínima de soja seja de 32 hectares. 
Formule e resolva o problema como um problema de programação linear.
'''

# Importando a biblioteca de otimização

from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Feijão", 0)                                    # Criação da variável de decisão
x2 = LpVariable("Soja", 0)                                      # Criação da variável de decisão

prob += 1600*x1 + 2500*x2                                      # Função objetivo
prob += x1 + x2 <= 80                                           # Restrição de produção
prob += x1 >= 20                                                # Restrição de quantidade mínima de feijão
prob += x2 >= 32                                                # Restrição de quantidade mínima de soja

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo
