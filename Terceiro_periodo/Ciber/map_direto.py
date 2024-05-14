def inicializar_cache(tam_cache):
    cache = {}
    for i in range(tam_cache):
        cache[i] = -1
    return cache

def imprimir_cache(cache):
    print(f"{'Posição da Memória':<20} | {'Valor':<10}")
    print("-" * 35)
    for posicao, valor in cache.items():
        print(f"{posicao:<20} | {valor:<10}")

