import random # Importa o módulo 'random' para gerar números aleatórios, essenciais para a inicialização e a mutação da população.

# Função simples para otimização (exemplo: f(x) = x^2)
def funcao(x):
    # Define a função objetivo que o algoritmo tentará minimizar.
    # Neste exemplo, o mínimo global é 0, que ocorre em x = 0.
    return x**2

# Algoritmo de busca populacional simples
def busca_populacional(iteracoes=50, tamanho_pop=10, limites=(-10, 10)):
    # Parâmetros: número de gerações, tamanho da população e o intervalo de busca para 'x'.
    
    # --- Inicialização da População ---
    populacao = [random.uniform(limites[0], limites[1]) for _ in range(tamanho_pop)]
    # Cria a população inicial com 'tamanho_pop' indivíduos.
    # Cada indivíduo é um número 'x' aleatório dentro dos 'limites' definidos.

    # --- Loop Principal da Otimização (Gerações) ---
    for _ in range(iteracoes):
        
        # 1. Avaliação
        avaliacoes = [(funcao(individuo), individuo) for individuo in populacao]
        # Avalia cada indivíduo da população, calculando o valor da função objetivo.
        # Armazena pares: (valor_da_funcao, individuo).
        
        avaliacoes.sort(key=lambda x: x[0])  # Ordena pelo valor da função (menor é melhor)
        # Ordena a lista de avaliações para identificar os melhores indivíduos.
        # Como é um problema de minimização, o menor valor da função é o "melhor".

        # 2. Seleção
        sobreviventes = [individuo for (_, individuo) in avaliacoes[:tamanho_pop // 2]]
        # Implementa uma estratégia de seleção: "elitismo".
        # Apenas os 'tamanho_pop // 2' (metade superior) melhores indivíduos sobrevivem para a próxima geração.

        # 3. Geração de novos indivíduos (Mutação Simples)
        nova_populacao = sobreviventes.copy()
        # A nova população começa com os indivíduos que sobreviveram (os pais).
        
        while len(nova_populacao) < tamanho_pop:
            # Loop para preencher a nova população até o tamanho original ('tamanho_pop').
            
            pai = random.choice(sobreviventes)
            # Seleciona aleatoriamente um indivíduo sobrevivente (pai) para reprodução.
            
            mutacao = pai + random.uniform(-1, 1)
            # Cria um novo indivíduo (filho) através de Mutação.
            # O filho é o pai mais um pequeno desvio aleatório entre -1 e 1.
            
            nova_populacao.append(mutacao)
            # Adiciona o novo indivíduo mutado à nova população.

        populacao = nova_populacao
        # A população para a próxima iteração é a recém-gerada.

    # --- Resultado Final ---
    melhor_x = min(populacao, key=funcao)
    # Após todas as iterações, encontra o melhor indivíduo na população final.
    
    return melhor_x, funcao(melhor_x)
    # Retorna o valor de 'x' que minimiza a função e o valor mínimo da função encontrado.

# Execução de exemplo
melhor_valor, melhor_funcao = busca_populacional()
print("Melhor valor encontrado (x):", melhor_valor)
print("Valor da função (f(x)):", melhor_funcao)