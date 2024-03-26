# Problemas de Pesquisa Operacional
# Problema apliacada lojistica de transporte
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Um fornecedor de armortecedores para automóveis dispõe de 10000 unidades em estoque e recebeu 4000 pedidos da indústria 1, 5000 pedidos da indústria 2 e 3000 
pedidos da indústria 3. O custo do amortecedor por peça para indústria 1 é R$ 5,00; para a indústria 2, R$ 7,00 e para a Indústria 3,
R$ 6,00. Sabendo que o objetivo do fornecedor é minimizar o custo total de transporte, determine quantas unidades deverão ser transportadas 
do fornecedor para cada uma das indústrias.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do transporte", LpMinimize)            # Criação do problema de minimização
x1 = LpVariable("Amortecedores para indústria 1",0)               # Criação da variável de decisão  
x2 = LpVariable("Amortecedores para indústria 2", 0)              # Criação da variável de decisão
x3 = LpVariable("Amortecedores para indústria 3", 0)              # Criação da variável de decisão
                                                                  # Observação: Neste porblema a demanda é maior do que a oferta
prob += 5*x1 + 7*x2 + 6*x3                                       # Função objetivo
prob += x1 + x2 + x3 >= 10000                                    # Restrição de quantidade de amortecedores disponíveis é menor do que a demanda
prob += x1 <= 4000                                               # Restrição de quantidade de amortecedores para a indústria 1
prob += x2 <= 5000                                               # Restrição de quantidade de amortecedores para a indústria 2
prob += x3 <= 3000                                               # Restrição de quantidade de amortecedores para a indústria 3

prob.solve()                                                      # Resolução do problema
for v in prob.variables():                                        # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective))                   # Impressão do valor da função objetivo



