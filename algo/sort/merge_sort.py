# coding=utf-8
def merge_sort(data, start, end):
    if start >= end:
        return
    mid = start + (end - start) // 2
    merge_sort(data, start, mid)
    merge_sort(data, mid + 1, end)
    merge_seq(data, start, mid, end)


def merge_seq(data, start, mid, end):
    data_tmp = []
    start1 = start
    start2 = mid + 1
    # merge tow sorted seq
    while start1 <= mid and start2 <= end:
        if data[start1] < data[start2]:
            data_tmp.append(data[start1])
            start1 += 1
        else:
            data_tmp.append(data[start2])
            start2 += 1
    # copy rest of seq1
    while start1 <= mid:
        data_tmp.append(data[start1])
        start1 += 1
    # copy rest of seq2
    while start2 <= end:
        data_tmp.append(data[start2])
        start2 += 1
    # copy data_tmp to data[start:end]
    for item in data_tmp:
        data[start] = item
        start += 1


data = [9, 4, 5, 1, 10, 2, 3]
merge_sort(data, 0, len(data) - 1)
print(data)