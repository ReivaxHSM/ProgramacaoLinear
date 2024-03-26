# Problemas de Pesquisa Operacional
# Calculadora de problemas de programação linear
# Autor: Heráclito Xavier
# Data: 23/03/2024

'''
Programa para resolver problemas de programação linear, definindo-se se é max ou min, quantidade de variáveis, 
coeficientes da função objetivo, quantidade de restrições, coeficientes das restrições e valores de b.
Ao inserir os coeficientes numa restrição, complete com zeros caso não haja coeficiente para uma variável. Por exemplo:
Para x1 <= 10, insira 1 0 (indicando um coeficiente 1 para x1 e 0 para x2).
Para x2 <= 15, insira 0 1 (indicando um coeficiente 0 para x1 e 1 para x2).
'''

from pulp import *                                                                                                                    # Importa a biblioteca PuLP para resolver problemas de programação linear

def pl_calculadora():                                                                                                                 # Função que inicia a calculadora de PL
    problema_tipo = input("Digite 'max' para maximização ou 'min' para minimização: ").strip().lower()                                # Solicita ao usuário definir se o problema é de maximização ou minimização
    problema = LpProblem("Meu_Problema_de_PL", LpMaximize if problema_tipo == "max" else LpMinimize)                                  # Cria o problema de programação linear
    
    n_variaveis = int(input("Informe a quantidade de variáveis de decisão: "))                                                        # Pede ao usuário a quantidade de variáveis de decisão
    variaveis = []                                                                                                                    # Lista para armazenar as variáveis de decisão
    for i in range(n_variaveis):                                                                                                      # Cria cada variável como não-negativa e a adiciona à lista
        var = LpVariable(f"x{i+1}", lowBound=0)                                                                                       # Variáveis são nomeadas como x1, x2, ..., xn
        variaveis.append(var)
    
    coef_objetivo = [float(coef) for coef in input("Informe os coeficientes da função objetivo separados por espaço: ").split()]      # Solicita ao usuário os coeficientes da função objetivo
    problema += lpSum([coef_objetivo[i] * variaveis[i] for i in range(n_variaveis)]), "Z"                                             # Define a função objetivo com os coeficientes fornecidos
    
    n_restricoes = int(input("Informe a quantidade de restrições: "))                                                                 # Pede ao usuário a quantidade de restrições do problema
    for i in range(n_restricoes):  
        coef_restricao = [float(coef) for coef in input(f"Restrição {i+1} - Informe os coeficientes separados por espaço: ").split()] # Para cada restrição, solicita os coeficientes
        b = float(input(f"Restrição {i+1} - Informe o valor de b: "))                                                                 # E o valor de b para a restrição
        relacao = input(f"Restrição {i+1} - Digite '<=' para <=, '>=' para >=, '=' para =: ").strip()                                 # Pergunta o tipo de relação da restrição (<=, >=, =)
                                                                                                                                      # Dependendo da relação, adiciona a restrição ao problema
        if relacao == "<=":                                                                                                           # Para relações <=, adiciona a restrição de que a soma deve ser menor ou igual a b
            problema += (lpSum([coef_restricao[j] * variaveis[j] for j in range(n_variaveis)]) <= b, f"restricao_{i+1}")              # Adiciona a restrição ao problema
        elif relacao == ">=":                                                                                                         # Para relações >=, adiciona a restrição de que a soma deve ser maior ou igual a b
            problema += (lpSum([coef_restricao[j] * variaveis[j] for j in range(n_variaveis)]) >= b, f"restricao_{i+1}")              # Adiciona a restrição ao problema
        elif relacao == "=":                                                                                                          # Para igualdades, adiciona a restrição de que a soma deve ser exatamente igual a b
            problema += (lpSum([coef_restricao[j] * variaveis[j] for j in range(n_variaveis)]) == b, f"restricao_{i+1}")              # Adiciona a restrição ao problema
    
    problema.solve()                                                                                                                  # Resolve o problema de programação linear
    
    print("Status:", LpStatus[problema.status])                                                                                       # Exibe o status da solução
    for v in problema.variables():                                                                                                    # Para cada variável, exibe o nome e o valor determinado na solução ótima
        print(v.name, "=", v.varValue)
   
    print("Valor da função objetivo (Z) =", value(problema.objective))                                                                # Exibe o valor da função objetivo na solução ótima

if __name__ == "__main__":                                                                                                            # Verifica se este script é o ponto de entrada principal
    pl_calculadora()                                                                                                                  # Executa a função que inicia a calculadora de PL


