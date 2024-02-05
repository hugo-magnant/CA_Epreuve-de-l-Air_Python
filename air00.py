import sys

def ma_fonction(s, sep):
    if s is None or sep is None:
        return []

    arr = []
    word = ""

    for char in s:
        if char in sep:
            if word:
                arr.append(word)
                word = ""
        else:
            word += char

    if word:
        arr.append(word)

    return arr

if len(sys.argv) != 2:
    print("error")
    sys.exit()

# Utilisation de la fonction avec des espaces, tabulations et retours à la ligne comme séparateurs
result = ma_fonction(sys.argv[1], " \t\n")
for word in result:
    print(word)
