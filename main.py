def div_k(lst, k):
    for nr in lst:
        if nr % k != 0:
            return False
    return True


def get_longest_div_k(lst, k):
    i = 1
    max_secv = []
    while i <= len(lst):
        for s in range(0, len(lst)-i+1):
            if div_k(lst[s:s+i], k):
                if len(lst[s:s+i]) > len(max_secv):
                    max_secv = lst[s:s+i]
        i += 1
    return max_secv


def main():
    lst_int = []
    while True:
        print('1. Pentru a citi numerele')
        print('2. Cea mai lunga secventa divizibila cu un k dat')
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
            print(f'cea mai lunga secventa cu toate numerele divizibile cu {k} este')
            list_div = get_longest_div_k(lst_int, k)
            print(list_div)
        elif optiune == 'x':
            break

main()
