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


def generate_square(size, colour=True):
    image = {   "type": "P1",
                "comment": "",
                "size": [],
                "pixels": []
            }
    # przypisz rozmiar [n, n]
    # wygeneruj kwadrat
        # dla n wierszy
            # dodaj n 0/1 (w zależności od colour) do wiersza (listy)
            # zapisz wiersz

    return image


def generate_diagonal(size):
    pass


def mirror_y(image):
    pass


def mirror_x(image):
    pass


def save_image(filename, image):
    """
        Saves an image to a filename.
    """

    outfile = open(filename, "w+")  # Open a filename in a write mode
    outfile.write(image["type"] + "\n")
    if image["comment"]:
        outfile.write(image["comment"] + "\n")  # Add comment if there is any
    outfile.write(' '.join(list(map(str, image["size"]))) + '\n')   # Change ints to strs and join them with spaces
    for row in image["pixels"]:
        outfile.write(' '.join(list(map(str, row))) + '\n') # Change ints to strs and join them with spaces

# print(generate_square(3, True))
image = {   "type": "P1",
                "comment": "komentarz",
                "size": [2, 3],
                "pixels": [ [1, 0], 
                            [0, 1],
                            [0, 1]]
            }

# image = load_image("nazwa_pliku")
save_image("test.pgm", image)