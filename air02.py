import sys

def ma_fonction(array_de_strings, separateur):
    if array_de_strings is None or len(array_de_strings) == 0 or separateur is None:
        print('error')
        sys.exit(1)

    result = ""
    for index, str in enumerate(array_de_strings):
        result += str
        if index != len(array_de_strings) - 1:
            result += separateur

    return result

if len(sys.argv) < 3:
    print('error')
    sys.exit(1)

# On extrait le tableau de chaînes et le séparateur des arguments du script.
# Le dernier argument est considéré comme le séparateur, et les autres comme le tableau de chaînes.
array_input = sys.argv[1:-1]
separator = sys.argv[-1]

output = ma_fonction(array_input, separator)
print(output)
