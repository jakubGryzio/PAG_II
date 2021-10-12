import math

def program1(tab, numb=None):
    for i in range(len(tab)):
        if numb - tab[i] in tab[i + 1:]:
            return True
    return False

def print_prime(tab, null_tab):
    print([tab[i] for i in range(len(null_tab)) if null_tab[i] == 0])

def program2(tab):
    tab = sorted(tab)
    zero_tab = [0 for _i in tab]
    for i in range(int(math.sqrt(len(tab))) + 1):
        for j in range(i+1, len(tab)):
            if tab[j] % tab[i] == 0:
                zero_tab[j] = 1
    print_prime(tab, zero_tab)

def program3(file):
    useless_char = ['(', ')', ',', '.', '!', ';', '–', '?']
    with open(file, 'r', encoding='utf-8') as f:
        words = "".join(f.readlines())
    for ch in useless_char:
        if ch in words:
            words = words.replace(ch, "")
    words = words.split(' ')
    count_words = {word: words.count(word) for word in words}
    sort_word = sorted(count_words.items(), key=lambda item: item[1], reverse=True)
    for word, num in sort_word:
        print(word, num)


program3(r'C:\Users\01150208\OneDrive - Politechnika Warszawska\Pliki_Kuby\Studia\III_ROK\PAG\PAG_II\tekst.txt')
