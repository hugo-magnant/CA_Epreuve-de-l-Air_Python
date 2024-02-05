import sys

def sorted_fusion(array1, array2):
    return sorted(array1 + array2)

if len(sys.argv) < 4 or "fusion" not in sys.argv:
    print('error')
    sys.exit(1)

fusion_index = sys.argv.index('fusion')

# Convertit les éléments avant et après 'fusion' en entiers.
try:
    array1 = [int(arg) for arg in sys.argv[1:fusion_index]]
    array2 = [int(arg) for arg in sys.argv[(fusion_index + 1):]]
except ValueError:
    print('error')
    sys.exit(1)

new_array = sorted_fusion(array1, array2)

print(' '.join(map(str, new_array)))
