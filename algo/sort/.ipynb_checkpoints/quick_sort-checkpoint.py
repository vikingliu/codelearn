# coding=utf-8


def partition(data, start, end):
    v = data[start]
    while start < end:
        while start < end and data[end] > v:
            end -= 1
        if start < end:
            data[start] = data[end]
        while start < end and data[start] <= v:
            start += 1
        if start < end:
            data[end] = data[start]
    data[start] = v
    return start


def partition_1(a, start, end):
    index = start
    start += 1
    while start < end:
        while start < end and a[end] > a[index]:
            end -= 1
        while start < end and a[start] < a[index]:
            start += 1
        a[start], a[end] = a[end], a[start]

    if a[start] > a[index]:
        start -= 1
    a[start], a[index] = a[index], a[start]
    return start


def partition_2(a, start, end):
    v = a[start]
    index = start
    for i in range(start + 1, end + 1):
        if a[i] < v:
            a[index] = a[i]
            index += 1
            a[i] = a[index]
    a[index] = v
    return index


def partition_3(a, start, end):
    v = a[end]
    index = end
    for i in range(end - 1, start - 1, -1):
        if a[i] > v:
            a[index] = a[i]
            index -= 1
            a[i] = a[index]
    a[index] = v
    return index


def quick_sort(data, start, end, func=partition):
    if start >= end:
        return

    p = func(data, start, end)
    quick_sort(data, start, p - 1)
    quick_sort(data, p + 1, end)


num = [5, 1, 9, 2, 4]
num = [8, 2, 5, 9, 10, 1, 4]
quick_sort(num, 0, len(num) - 1, partition)
print(num)
