def inicializar_cache(tam_cache):
    cache = {}
    for i in range(tam_cache):
        cache[i] = -1
    return cache

def imprimir_cache(cache):
    print(f"{'Pos Cache':<10} | {'Pos Memória':<10}")
    print("-" * 25)
    for posicao, valor in cache.items():
        print(f"{posicao:>10} | {valor:>10}")

def mapeamento_direto(tam_cache, pos_memoria):
    cache = inicializar_cache(tam_cache)
    print("Cache Inicial")
    print(f"{'Tam Cache: ':<10} {tam_cache:<10}")
    imprimir_cache(cache)

    hits = 0
    misses = 0

    for i in range(len(pos_memoria)):
        pos_cache = pos_memoria[i] % tam_cache

        print(f"Linha {pos_cache} | Posição da memória {pos_memoria[i]}")

        if cache[pos_cache] == pos_memoria[i]:
            hits += 1
            print("Status: Hit")
        else:
            misses +=1
            print("Status: Miss")
            cache[pos_cache] = pos_memoria[i]
        
        imprimir_cache(cache)

    print(f"Total de Misses: {misses}")
    print(f"Total de Hits: {hits}")

mapeamento_direto(5, [33,3,11,5])     