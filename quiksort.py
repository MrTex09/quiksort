def particion(arr, bajo, alto):
    i = bajo - 1  # Índice del elemento más pequeño
    pivote = arr[alto]  # Pivote

    for j in range(bajo, alto):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambia

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1
