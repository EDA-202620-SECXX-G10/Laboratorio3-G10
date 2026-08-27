import random
def new_list():
    newlist ={
        'elements' : [],
        'size' : 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list['elements'][index-1]

def is_present(my_list, element, cmp_function):
    
    size = my_list['size']
    if size > 0:
        keyexist = False 
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(info, element) == 0:
                keyexist = True
                break
            if keyexist:
                return keypos
    return -1

def is_empty(my_list):
    return my_list["size"] == 0

def size(my_list):
    return my_list["size"]

def last_element(my_list):
    return my_list["elements"][my_list["size"]-1]

def delete_element(my_list, pos):
    del my_list["elements"][pos]
    my_list["size"] -= 1
    return my_list
    
def remove_first(my_list):
    del my_list["elements"][0]
    my_list["size"] -=1
    return my_list 

def remove_last(my_list):
    del my_list["elements"][my_list["size"]-1]
    my_list["size"] -= 1
    return my_list

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list 

def change_info(my_list, new_info, pos):
    my_list["elements"][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    temporal = my_list["elements"][pos_1]
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    my_list["elements"][pos_2] = temporal
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def sub_list(my_list, pos_i, num_elements):
    newlist = new_list()
    for i in range(pos_i, pos_i + num_elements):
        insert_element(newlist, my_list["elements"][i], size(newlist))
    return newlist


def default_sort_criteria(element1, element2):
    is_sorted = False
    if element1 <= element2:
        is_sorted = True
    return is_sorted

def insertion_sort(lista, default_sort_criteria):
    tamanio = size(lista)

    for i in range(2, tamanio + 1):
        j = i

        while j > 1 and default_sort_criteria(get_element(lista, j), get_element(lista, j - 1)):
            exchange(lista, j, j - 1)
            j -= 1

    return lista

def selection_sort(my_list, sort_crit):
    n = my_list["size"]
    elements = my_list["elements"]
    for i in range(n-1):
        min_index = i
        for j in range(i + 1,n):
            if sort_crit(elements[j], elements[min_index]):
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]

    return my_list

def shell_sort(my_list, default_sort_criteria):
    size = my_list["size"]
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = my_list["elements"][i]
            j = i
            while j >= gap and default_sort_criteria(my_list["elements"][j - gap], temp) == False:
                my_list["elements"][j] = my_list["elements"][j - gap]
                j -= gap
            my_list["elements"][j] = temp
        gap //= 2
    return my_list

def merge_sort(my_list, sort_criteria):
    elementos = my_list["elements"]
    n = len(elementos)

    def mezclar(inicio, medio, fin, auxiliar):
        i = inicio
        j = medio + 1
        k = inicio

        while i <= medio and j <= fin:
            if sort_criteria(elementos[i], elementos[j]):
                auxiliar[k] = elementos[i]
                i += 1
            else:
                auxiliar[k] = elementos[j]
                j += 1
            k += 1

        while i <= medio:
            auxiliar[k] = elementos[i]
            i += 1
            k += 1

        while j <= fin:
            auxiliar[k] = elementos[j]
            j += 1
            k += 1

        for pos in range(inicio, fin + 1):
            elementos[pos] = auxiliar[pos]

    def ordenar(inicio, fin, auxiliar):
        if inicio < fin:
            medio = (inicio + fin) // 2
            ordenar(inicio, medio, auxiliar)
            ordenar(medio + 1, fin, auxiliar)
            mezclar(inicio, medio, fin, auxiliar)

    if n > 1:
        auxiliar = elementos.copy()
        ordenar(0, n - 1, auxiliar)

    return my_list

def quick_sort(my_list, sort_criteria):
    elementos = my_list["elements"]
    n = len(elementos)

    def dividir(lo, hi):
        pivote = elementos[lo]
        i = lo + 1
        j = hi
        terminado = False

        while not terminado:
            while i <= hi and sort_criteria(elementos[i], pivote):
                i += 1
            while j >= lo + 1 and sort_criteria(pivote, elementos[j]):
                j -= 1
            if i >= j:
                terminado = True
            else:
                elementos[i], elementos[j] = elementos[j], elementos[i]
                i += 1
                j -= 1

        elementos[lo], elementos[j] = elementos[j], elementos[lo]
        return j

    def ordenar(lo, hi):
        if lo < hi:
            posicion_pivote = dividir(lo, hi)
            ordenar(lo, posicion_pivote - 1)
            ordenar(posicion_pivote + 1, hi)

    if n > 1:
        random.shuffle(elementos)
        ordenar(0, n - 1)

    return my_list