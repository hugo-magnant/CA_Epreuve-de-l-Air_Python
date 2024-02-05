import sys

if len(sys.argv) != 2:
    print("error")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("error")
    sys.exit(1)
