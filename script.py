# Ten skrypt sprawdza, ile słów (i jakie dokładnie) powtórzyło się
# co najmniej raz w każdym z poniższych plików

FILES = ["file1.txt", "file2.txt", "file3.txt"]

all_words = {}
#otwórz po kolei wszystkie pliki
for file in FILES:
    f = open(file, "r")
    #odczytaj wszystkie unikalne słowa
    words = set()
    for line in f:
        for word in line.split():
            words.add(word)
    
    #zapisz, że w pliku wystąpiły te słowa
    for word in words:
        if word in all_words:
            all_words[word] += 1
        else:
            all_words[word] = 1

AMOUNT_OF_FILES = len(FILES)
total_words = 0
#sprawdź, ile i jakie słowa wystąpiły we wszystkich plikach
print("\nSłowa, które wystąpiły co najmniej raz w każdym pliku:")
for word in all_words:
    if all_words[word] == AMOUNT_OF_FILES:
        total_words += 1
        print(" -", word)
        
print("Łączna ilość takich słów:", total_words)



            
