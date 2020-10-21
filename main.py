

def load_image(filename):
    image = {   "type": "P1",
                "comment": "komentarz",
                "size": [2, 3],
                "pixels": [ [1, 0], 
                            [0, 1],
                            [0, 1]]
            }
    return image


def save_image(filename, image):
    pass

image = load_image("nazwa_pliku")
save_image("inna_nazwa", image)