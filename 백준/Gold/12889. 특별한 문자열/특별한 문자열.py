def special_checker(string):
    for idx in range(1, len(string)):
        left_string = string[:idx]
        right_string = string[idx:]
        if left_string >= right_string:
            return False
    return True


def next_string_finder(special_string):
    length = len(special_string)
    special_string = list(special_string)
    for idx in range(length - 1, -1, -1):
        if special_string[idx] == '1':
            continue
        next_string = special_string[:]

        for next_idx in range(idx, length):
            next_string[next_idx] = '1'

        if not special_checker(next_string):
            continue

        for next_idx in range(idx + 1, length):
            next_string[next_idx] = '0'
            if not special_checker(next_string):
                next_string[next_idx] = '1'

        return ''.join(next_string)

    return '-1'


special_string = list(input())
print(next_string_finder(special_string))
