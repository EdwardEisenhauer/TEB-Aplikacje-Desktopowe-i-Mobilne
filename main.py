def load_image(filename):
    image = {   "type": "P1",
                "comment": "komentarz",
                "size": [2, 3],
                "pixels": [ [1, 0], 
                            [0, 1],
                            [0, 1]]
            }
    # Otworzyć plik
    # Wczytać nagłówki do odpowiednich stron słownika
    # Na podstawie rozmiaru wczytać piksele
    return image


def save_image(filename, image):
    # Otowrzyć plik
    # Zapisać nagłówki ze słownika do pliku
    # Na podstawie rozmiaru zapisać piksele
    pass

image = load_image("nazwa_pliku")
save_image("inna_nazwa", image)