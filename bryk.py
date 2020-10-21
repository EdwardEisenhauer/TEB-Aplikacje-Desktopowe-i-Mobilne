#############################
## Typy danych
## Więcej na: https://github.com/Parodix007/PythonClass
#############################

image = {   "type": "P1",
            "comment": "komentarz",
            "size": [2, 3],
            "pixels": [ [1, 0], 
                        [0, 1],
                        [0, 1]]
        }

# RZUTOWANIE

str(23) # => "23"

##################################################
## Przepływ sterowania (ify, switche itp.) i pętle
##################################################

if (False):
    print("To się nie wykona")
elif (0):
    print("To też się nie wykona")
else:
    print("A to już tak")


for i in range(10):
    print(i)        # Wydrukuje nam liczby od 0 do 9

while (True):
    print("To będzie się printowało w nieskończoność")

#############################
## Operacje wejścia i wyjścia
#############################

# TERMINAL

print("String, który pojawi się na ekranie") # Nie używamy polskich znaków!
variable = input("Prompt, który pojawi się na ekranie")

# PLIKI

# funkcja open(file, mode) służy do otwierania (tworzenia) plików
# r - read (czytanie)
# w - write (pisanie)
# + - aktualizowane, dodawanie treści na końcu pliku
file = open("plik1", "r") # otworzyliśmy plik1 w trybie czytania
file = open("plik2", "w+") # otworzyliśmy plik2 w trypie aktualizowania

file.write("string do zapisania w pliku")
flie.write("Ważna liczba: " + str(2122))

#############################
## Funkcje
#############################

# def - definicja funkcji
# load_image - nazwa funkcji
# filename - argument funkcji

def load_image(filename):
    return image            # zwraca zmienną image