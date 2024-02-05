import sys

def sorted_insert(array, new_element):
    array.append(new_element)
    return sorted(array)

if len(sys.argv) < 3 or not all(arg.isdigit() for arg in sys.argv[1:]):
    print('error')
    sys.exit(1)

new_element = int(sys.argv[-1])
array = [int(arg) for arg in sys.argv[1:-1]]

new_array = sorted_insert(array, new_element)

print(' '.join(map(str, new_array)))
