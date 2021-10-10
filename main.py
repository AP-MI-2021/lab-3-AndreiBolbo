def div_k(lst, k):
    """
     verifica daca toate elementele unei liste sunt diviizbile cu un k dat
     -Input:lst:lista[int],k(int)
     -Output:True/False
    """
    for nr in lst:
        if nr % k != 0:
            return False
    return True


def get_longest_div_k(lst, k):
    """
    determina secventa cea mai lunga divizibila cu k
    -Input:lst:-lista[int],k(int)
    -Output:max_secv:-lista[int]
    """
    i = 1
    max_secv = []
    while i <= len(lst):
        for s in range(0, len(lst)-i+1):
            if div_k(lst[s:s+i], k):
                if len(lst[s:s+i]) > len(max_secv):
                    max_secv = lst[s:s+i]
        i += 1
    return max_secv


def arithmetic_progression(lst):
    """
    verifica daca elementele listei sunt in progresie aritmetica
    -Input: lst:lista[int]
    -Output: True/False
    """
    for i in range(1, len(lst)-1):
        if lst[i] != (lst[i-1]+lst[i+1])/2:
            return False
    return True


def get_longest_arithmetic_progression(lst):
    """
    Determina secventa maxima aflata in progresie aritmetica
    prin compararea lungimilor a listelor cu aceasta proprietate
    -Input: lst:list[int]
    -Output: max_secv:list[int]
    """
    lista_secv = []
    for start in range(0, len(lst)-2):
        for stop in range(start+3, len(lst)+1):
            if arithmetic_progression(lst[start:stop]):
                lista_secv.append(lst[start:stop])
    max_secv = []
    for secventa in lista_secv:
        if len(secventa) > len(max_secv):
            max_secv = secventa
    return max_secv


def test_longest_div_k():
    assert get_longest_div_k([1, 2, 4, 6], 2) == [2, 4, 6]
    assert get_longest_div_k([1, 2, 4, 6], 3) == [6]
    assert get_longest_div_k([1, 2, 4, 6], 1) == [1, 2, 4, 6]
    assert get_longest_div_k([1, 2, 4, 6], 7) == []
    assert get_longest_div_k([1, 2, 4, 6, 8, 9], 3) == [6]
    assert get_longest_div_k([1, 2, 4, 6, 8], 9) == []


def main():
    lst_int = []
    while True:
        print('1. Pentru a citi numerele')
        print('2. Cea mai lunga secventa divizibila cu un k dat')
        print('3. Cea mai lunga secventa in progresie aritmetica')
        print('x. Pentru a iesi ')
        optiune = input('alegeti optiunea dorita :')
        if optiune == '1':
            lst_int = []
            lst_string = input('dati numerele separate printr-un spatiu :')
            lst_sep = lst_string.split(' ')
            for element in lst_sep:
                lst_int.append(int(element))
        elif optiune == '2':
            k = int(input('dati un k :'))
            print(f'cea mai lunga secventa cu toate numerele divizibile cu {k} este:')
            list_div = get_longest_div_k(lst_int, k)
            if list_div != []:
                print(list_div)
            else:
                print(f'Nu exista niciun numar divizibil cu {k}')
        elif optiune == '3':
            list_arit = get_longest_arithmetic_progression(lst_int)
            if list_arit != []:
                print(f'cea mai lunga secventa cu numerele in progresie aritmetica este : {list_arit}')
            else:
                print('Nu exista')
        elif optiune == 'x':
            break
        else:
            print('Optiune incorecta')


test_longest_div_k()
main()
