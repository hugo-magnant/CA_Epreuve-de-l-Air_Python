import sys

if len(sys.argv) != 3:
    print("error")
    sys.exit(1)

char = sys.argv[1]
try:
    height = int(sys.argv[2])
except ValueError:
    print("error")
    sys.exit(1)

if height <= 0:
    print("error")
    sys.exit(1)

for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    chars = char * (2 * i - 1)
    print(f"{spaces}{chars}")
