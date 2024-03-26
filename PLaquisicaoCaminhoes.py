# Problemas de Pesquisa Operacional
# Problema apliacado a aquisição de caminhões
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Uma transportadora precisa ampliar a sua capacidade de entregas e está estudando a viabilidade da compra de três novos caminhões. 
O custo para a aquisição de um caminhão grande é de R$ 3,4 milhões, R$ 2,1 milhões para um caminhão médio e $ 1,9 milhões para 
a compra de um caminhão pequeno. O orçamento destinado à compra desses caminhões é de R$ 80 milhões. Com base nos valores atuais 
dos fretes, o lucro anual líquido estimado para a compra dos novos caminhões será de R$ 80.000,00 para cada caminhão grande, 
R$ 67.000,00 para cada caminhão médio e R$ 36.000,00 para cada caminhão pequeno. A transportadora precisa adquirir 
pelo menos quatro caminhões de cada tipo. Como o objetivo é determinar quantos caminhões de cada tipo devem ser adquiridos para 
maximizar o lucro anual, formule e resolva o problema como um problema de programação linear.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Caminhao grande", 0)                           # Criação da variável de decisão
x2 = LpVariable("Caminhao medio", 0)                            # Criação da variável de decisão
x3 = LpVariable("Caminhao pequeno", 0)                          # Criação da variável de decisão

prob += 80000*x1 + 67000*x2 + 36000*x3                          # Função objetivo
prob += 3400000*x1 + 2100000*x2 + 1900000*x3 <= 80000000        # Restrição de orçamento
prob += x1 >= 4                                                 # Restrição de quantidade mínima de caminhões grandes
prob += x2 >= 4                                                 # Restrição de quantidade mínima de caminhões médios
prob += x3 >= 4                                                 # Restrição de quantidade mínima de caminhões pequenos

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo