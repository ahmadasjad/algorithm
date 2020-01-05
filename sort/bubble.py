

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        inner_swapped = False
        for inner_index in range(n-(i+1)):
            if data[inner_index] > data[inner_index+1]:
                data[inner_index], data[inner_index+1] = data[inner_index+1], data[inner_index]
                inner_swapped = True
        if not inner_swapped:
            break


if __name__ == '__main__':
    data = list(map(int, input('Enter space separated integers: ').split()))
    print('befor sort: ', data)
    bubble_sort(data)
    print('after sort: ', data)
