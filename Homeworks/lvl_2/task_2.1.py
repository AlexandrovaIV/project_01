# Задача 2.1.

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

arr = [[4, 6, 2, 1, 9, 63, -134, 566], [-52, 56, 30, 29, -54, 0, -110], [42, 54, 65, 87, 0], [5]]


def choice(data):
    i = 0
    length = len(data)
    while i < length - 1:
        m = i
        j = i + 1
        while j < length:
            if data[j] < data[m]:
                m = j
            j += 1
        data[i], data[m] = data[m], data[i]
        i += 1
    return data


def minimum(arrr):
    print('МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ')
    for data in arrr:
        print('Минимальные значение из массива: ', data, choice(data)[0])


def maximum(arrr):
    print('МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ')
    for data in arrr:
        print("Максимальное значение из массива: ", data, choice(data)[len(data) - 1])


def main():
    minimum(arr)
    maximum(arr)


main()
