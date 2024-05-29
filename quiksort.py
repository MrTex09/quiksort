def particion(arr, bajo, alto):
    i = bajo - 1  # Índice del elemento más pequeño
    pivote = arr[alto]  # Pivote seleccionado como el último elemento

    for j in range(bajo, alto):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiar

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quicksort(arr, bajo, alto):
    if bajo < alto:
        # pi es el índice de partición, arr[pi] está en la posición correcta
        pi = particion(arr, bajo, alto)
        # Ordenar recursivamente los elementos antes y después de la partición
        quicksort(arr, bajo, pi - 1)
        quicksort(arr, pi + 1, alto)
def ordenar(arr):
    quicksort(arr, 0, len(arr) - 1)



