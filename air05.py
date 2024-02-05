import sys

def apply_operation(numbers, operation):
    operator = operation[0]
    try:
        operand = int(operation[1:])

        if operator == '+':
            return [num + operand for num in numbers]
        elif operator == '-':
            return [num - operand for num in numbers]
        else:
            return 'error'
    except ValueError:
        return 'error'

if len(sys.argv) < 3:
    print('error')
    sys.exit(1)

operation = sys.argv[-1]
try:
    numbers = [int(arg) for arg in sys.argv[1:-1]]
except ValueError:
    print('error')
    sys.exit(1)

result = apply_operation(numbers, operation)

if result == 'error':
    print('error')
    sys.exit(1)
else:
    print(' '.join(map(str, result)))
