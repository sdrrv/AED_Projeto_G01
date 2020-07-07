

def quicksort(self, l, r, comp):
    i = left
    j = right
    pivot = l[int((i+j)/2)]
    while i <= j:
        while comp(l[i], pivot) and i < len(l):
            i += 1
        while comp(pivot, l[j]) and j > -1:
            j -= 1
        if i <= j:
            tmp = l[j]
            l[j] = l[i]
            l[i] = tmp
            i += 1
            j -= 1
        if left < j:
            quicksort(l, left, j, comp)
        if i < right:
            quicksort(l, i, right, comp)


def comp_numbers(a, b):
    return a < b


def sorting_func(array):

    # Fazer uma funçao de comparaçao que veja se tiver nao tiver familia aparece primeiro , depois olha para as faixas etaria e desempata
    # com ordem alfabética , assim so tenho de chamar quicksort na lista de objetos
