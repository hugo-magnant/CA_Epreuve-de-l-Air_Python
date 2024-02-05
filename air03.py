import sys

def find_single_element(array):
    if array is None or len(array) == 0:
        print('error')
        sys.exit(1)

    frequency = {}

    for elem in array:
        frequency[elem] = frequency.get(elem, 0) + 1

    return next((k for k, v in frequency.items() if v == 1), 'error')

if len(sys.argv) == 1:
    print('error')
    sys.exit(1)

result = find_single_element(sys.argv[1:])
if result == 'error':
    print('error')
    sys.exit(1)
else:
    print(result)
