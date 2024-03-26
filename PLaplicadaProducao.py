# Problemas de Pesquisa Operacional
# Problema do canos
# Autor: Heráclito Xavier
# Data: 23/03/2024

# A produção de uma indústria de artigos esportivos consiste na fabricação de blusões e de calças em um único tamanho.
# Para a produção de cada blusão, a indústria utiliza 1,2 metros de tecido e, para a produção de cada calça, utiliza 1,3 metros 
# deste mesmo tecido. Em virtude de máquinas e de mão de obra, a produção máxima é de 800 blusões e de 900 calças.
# A quantidade máxima de tecido disponível por dia é igual a 2000 metros. Foi informado que o lucro referente à venda de 
# cada blusão é de R$ 75,00. e o lucro referente à venda de cada calça corresponde a R$ 60,00. O objetivo da indústria é determinar quantas
# unidades de cada produto devem ser produzidos diariamente de modo que o lucro seja o maior possível.
# Formule e resolva o problema como um problema de programação linear.

# Importando a biblioteca de otimização
from pulp import *

prob = LpProblem("Problema da produção", LpMaximize)            # Criação do problema de maximização
x1 = LpVariable("Blusão", 0)                                    # Criação da variável de decisão
x2 = LpVariable("Calca", 0)                                     # Criação da variável de decisão

prob += 75*x1 + 60*x2                                           # Função objetivo
prob += 1.2*x1 + 1.3*x2 <= 2000                                 # Restrição de produção
prob += x1 <= 800                                               # Restrição de quantidade máxima de blusões
prob += x2 <= 900                                               # Restrição de quantidade máxima de calças

prob.solve()                                                    # Resolução do problema
for v in prob.variables():                                      # Impressão das variáveis de decisão
    print(v.name, "=", v.varValue)                              # Impressão das variáveis de decisão

print("Lucro máximo = ", value(prob.objective))                 # Impressão do valor da função objetivo

# Resultado

