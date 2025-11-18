import random

# Função simples para otimização (exemplo: f(x) = x^2)
def funcao(x):
    return x**2

# Algoritmo de busca populacional simples
def busca_populacional(iteracoes=50, tamanho_pop=10, limites=(-10, 10)):
    populacao = [random.uniform(limites[0], limites[1]) for _ in range(tamanho_pop)]

    for _ in range(iteracoes):
        # Avaliação
        avaliacoes = [(funcao(individuo), individuo) for individuo in populacao]
        avaliacoes.sort(key=lambda x: x[0])  # Ordena pelo valor da função (menor é melhor)

        # Seleciona a metade superior (os melhores)
        sobreviventes = [individuo for (_, individuo) in avaliacoes[:tamanho_pop // 2]]

        # Geração de novos indivíduos (mutação simples)
        nova_populacao = sobreviventes.copy()
        while len(nova_populacao) < tamanho_pop:
            pai = random.choice(sobreviventes)
            mutacao = pai + random.uniform(-1, 1)
            nova_populacao.append(mutacao)

        populacao = nova_populacao

    # Melhor resultado
    melhor_x = min(populacao, key=funcao)
    return melhor_x, funcao(melhor_x)

# Execução de exemplo
melhor_valor, melhor_funcao = busca_populacional()
print("Melhor valor encontrado:", melhor_valor)
print("Valor da função:", melhor_funcao)
