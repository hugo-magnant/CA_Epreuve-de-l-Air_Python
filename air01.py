import sys

def ma_fonction(str_to_cut, separator):
    if str_to_cut is None or separator is None or separator == "":
        print('error')
        sys.exit(1)

    result = []
    start_idx = 0

    while start_idx < len(str_to_cut):
        end_idx = str_to_cut.find(separator, start_idx)
        if end_idx == -1:
            result.append(str_to_cut[start_idx:])
            break
        else:
            result.append(str_to_cut[start_idx:end_idx])
            start_idx = end_idx + len(separator)

    return result

if len(sys.argv) != 3:
    print('error')
    sys.exit(1)

input_str = sys.argv[1]
separator = sys.argv[2]

output = ma_fonction(input_str, separator)
for item in output:
    print(item)
