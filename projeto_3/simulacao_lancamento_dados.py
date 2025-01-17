from random import randint
from collections import Counter

def lancar_dados(quantidade: int) -> list:
    """
    Simula a jogada de 2 dados de 6 lados e guarda os resultados em uma lista.

    Args:
        quantidade (int): Número de vezes que os dados são lançados.

    Returns:
        list: Lista de tuplas com os resultados.
    """
    return [(randint(1, 6), randint(1, 6)) for _ in range(quantidade)]

def somar_resultados(resultados: list) -> list:
    """
    Soma os resultados de cada tupla na lista de resultados.

    Args:
        resultados (list): Lista de tuplas.

    Returns:
        list: Lista com os números somados.
    """
    return [a + b for a, b in resultados]

def encontrar_soma_mais_frequente(resultados_somados: list) -> int:
    """
    Encontra a soma mais frequente na lista de resultados.

    Args:
        resultados_somados (list): Lista dos resultados somados.

    Returns:
        int: A soma mais frequente.
    """
    soma_mais_frequente, _ = Counter(resultados_somados).most_common(1)[0]
    return soma_mais_frequente

def resultados_maiores_que_7(resultados_somados: list) -> int:
    """
    Conta quantas vezes os resultados somados foram maiores que 7.

    Args:
        resultados_somados (list): Lista dos resultados somados.

    Returns:
        int: A contagem final dos resultados maiores que 7.
    """
    return sum(1 for resultado in resultados_somados if resultado > 7)

def encontrar_combinacoes_mais_frequentes(resultados: list, top: int = 3) -> list:
    """
    Encontra as combinações mais frequentes de lançamentos.

    Args:
        resultados (list): Lista de tuplas com os resultados de lançamentos.
        top (int): Quantidade de combinações mais frequentes a retornar.

    Returns:
        list: Lista das combinações mais frequentes e suas frequências.
    """
    return Counter(resultados).most_common(top)

def main():
    # Simula 1000 lançamentos de dois dados
    resultados = lancar_dados(1000)
    
    # Calcula a soma dos lançamentos
    resultados_somados = somar_resultados(resultados)
    
    # Soma mais frequente
    soma_mais_frequente = encontrar_soma_mais_frequente(resultados_somados)
    
    # Número de somas maiores que 7
    maiores_que_7 = resultados_maiores_que_7(resultados_somados)
    
    # Três combinações mais frequentes
    combinacoes_mais_frequentes = encontrar_combinacoes_mais_frequentes(resultados)
    
    # Exibe os resultados
    print(f'Soma mais frequente: {soma_mais_frequente}')
    print(f'Número de resultados maiores que 7: {maiores_que_7}')
    print(f'Três combinações mais frequentes: {combinacoes_mais_frequentes}')

if __name__ == '__main__':
    main()
