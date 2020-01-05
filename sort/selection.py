

def selection_sort(data, start_pos):
    n = len(data)
    smallest_index = start_pos
    for i in range(start_pos+1, n):
        if data[i] < data[smallest_index]:
            smallest_index = i
    if smallest_index != start_pos:
        data[smallest_index], data[start_pos] = data[start_pos], data[smallest_index]
        selection_sort(data, start_pos+1)


if __name__ == '__main__':
    int_list = list(map(int, input('Enter space separated integers: ').split()))
    print('before sort: ', int_list)
    selection_sort(int_list, 0)
    print('after sort: ', int_list)
