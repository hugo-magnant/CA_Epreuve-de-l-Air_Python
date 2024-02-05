import sys

def remove_adjacent_duplicates(s):
    if s is None or s == "":
        return 'error'

    new_str = ''
    last_char = None

    for char in s:
        if char != last_char:
            new_str += char
            last_char = char

    return new_str

if len(sys.argv) != 2:
    print('error')
    sys.exit(1)

input_str = sys.argv[1]
result = remove_adjacent_duplicates(input_str)

if result == 'error':
    print('error')
    sys.exit(1)
else:
    print(result)
