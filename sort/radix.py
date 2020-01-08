
def radix_sort(data):
    digits = len(str(max(data)))
    data = ["{:02d}".format(i) for i in data]
    for digit_pos in range(digits-1, -1, -1):
        new_digits = []
        for i in range(10):
            for item in data:
                if str(item)[digit_pos] == str(i):
                    new_digits.append(item)
        data = new_digits
    return list(map(int, data))


if __name__ == '__main__':
    int_list = list(map(int, input('Enter space separated integer list: ').split()))
    sorted_int = radix_sort(int_list)
    print(sorted_int)
