def particion(arr, bajo, alto):
    i = bajo - 1  # Índice del elemento más pequeño
    pivote = arr[alto]  # Pivote seleccionado como el último elemento

    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiar

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quicksort(arr, bajo, alto):
    if bajo < alto:
        pi = particion(arr, bajo, alto)
        quicksort(arr, bajo, pi - 1)
        quicksort(arr, pi + 1, alto)

def ordenar(arr):
    quicksort(arr, 0, len(arr) - 1)

def pruebas():
    # Lista de ejemplo 1 lista desordenada con números positivos y negativos
    lista1 = [34, -2, 78, 0, -42, 8, 19, 3]
    print("Lista original 1:", lista1)
    ordenar(lista1)
    print("Lista ordenada 1:", lista1)

    # Lista de ejemplo 2: Lista ya ordenada
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Lista original 2:", lista2)
    ordenar(lista2)
    print("Lista ordenada 2:", lista2)

    # Lista de ejemplo 3: Lista en orden inverso
    lista3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Lista original 3:", lista3)
    ordenar(lista3)
    print("Lista ordenada 3:", lista3)
