# coding = utf-8


def bubble(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr


if __name__ == '__main__':
    L = [4, 9, 10, 5, 111, 3, 244]
    print(bubble(L))
    print(L)
