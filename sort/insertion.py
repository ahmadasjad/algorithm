
def insertion_sort(data):
    n = len(data)
    for key_index in range(1, n):
        for i in range(key_index, -1, -1):
            if i == 0 or data[i] > data[i-1]:
                break
            data[i], data[i-1] = data[i-1], data[i]


if __name__ == '__main__':
    int_list = list(map(int, input('Enter space separated integers: ').split()))
    print('befor sort: ', int_list)
    insertion_sort(int_list)
    print('after sort: ', int_list)
