import sys

def ma_rotation(array):
    if not array:
        return array
    
    first_element = array.pop(0)
    array.append(first_element)
    return array

if len(sys.argv) == 1:
    print('error')
    sys.exit(1)

rotated_array = ma_rotation(sys.argv[1:])  # On ignore le premier argument car c'est le nom du script

print(', '.join(rotated_array))
