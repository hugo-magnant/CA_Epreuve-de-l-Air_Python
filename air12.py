import sys

def my_quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    less = []
    greater = []
    
    for element in array[1:]:
        if element <= pivot:
            less.append(element)
        else:
            greater.append(element)
    
    return my_quick_sort(less) + [pivot] + my_quick_sort(greater)

if len(sys.argv) == 1:
    print("error")
    sys.exit(1)

try:
    input_array = [int(x) for x in sys.argv[1:]]
except ValueError:
    print("error")
    sys.exit(1)

sorted_array = my_quick_sort(input_array)
print(" ".join(map(str, sorted_array)))
