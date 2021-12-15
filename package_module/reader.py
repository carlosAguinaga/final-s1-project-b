
def get_words(file_name: str)-> list:
    with open(file_name) as historia:
        lineas = historia.readlines()
        lineas = [i.replace('\n', '') for i in lineas]
        words = []
        for linea in lineas:
            words = [*words, *linea.split(' ')]

        return words