# Problemas de Pesquisa Operacional
# Problema Aula Pratica 3.8 Fábrica de bicicletas
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Devido a alguns pedidos de revendedores, uma fábrica de biciletas precisa enviar 5000 uniddes para a revenda A, 3000 para a revenda B e 
4000 unidades para a revenda C. Atualmente, a fábrica tem à disposição 10000 unidades. Os custos unitários de transporte da fábrica para
as revendas A, B e C são, respectivamente, R$ 25,00, R$ 18,00 e R$ 22,00. Como a empresa deseja minimizar o custo total de transporte,
resolva o problema como um problema de programação linear.
'''

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema do transporte", LpMinimize)            # Criação do problema de minimização
x1 = LpVariable("Bicicletas para revenda A",0)                    # Criação da variável de decisão
x2 = LpVariable("Bicicletas para revenda B", 0)                   # Criação da variável de decisão
x3 = LpVariable("Bicicletas para revenda C", 0)                   # Criação da variável de decisão
                                                                  # Observação: Neste porblema a demanda é maior do que a oferta
prob += 25*x1 + 18*x2 + 22*x3                                     # Função objetivo
prob += x1 + x2 + x3 >= 10000                                     # Restrição de quantidade de bicicletas disponíveis é menor do que a demanda
prob += x1 <= 5000                                                # Restrição de quantidade de bicicletas para a revenda A
prob += x2 <= 3000                                                # Restrição de quantidade de bicicletas para a revenda B
prob += x3 <= 4000                                                # Restrição de quantidade de bicicletas para a revenda C

prob.solve()                                                      # Resolução do problema
for v in prob.variables():                                        # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                                # Impressão das variáveis de decisão

print("Custo mínimo = ", value(prob.objective))                   # Impressão do valor da função objetivo












