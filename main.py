import random
import time
import sys


def quicksort(A, low, high):
    if low < high:
        parti = lomutoPartition(A, low, high)
        quicksort(A, low, parti - 1)
        quicksort(A, parti + 1, high)


def lomutoPartition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if pivot >= A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1


def generator(n):
    A = []
    i = 0
    while (n > i):
        i = i + 1
        x = random.randint(0, 255)
        A.append(x)
    return A


def heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[largest] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]

        heapify(A, n, largest)


def heapSort(A):
    n = len(A)

    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)


def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


def mergeSort(A):
    if len(A) > 1:

        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    x = 500000
    sys.setrecursionlimit(x)
    A = generator(1000)  # gen for qs

    low, high = 0, len(A) - 1

    start = time.time()
    quicksort(A, low, high)
    stop = time.time()
    timer = stop - start
    print("QS RANDOM TIME:", timer)

    B = []
    C = []
    B = list(A)
    C = list(reversed(A))

    start = time.time()
    quicksort(B, low, high)
    stop = time.time()
    timer = stop - start
    print("QS SORTED TIME:", timer)

    start = time.time()
    quicksort(C, low, high)
    stop = time.time()
    timer = stop - start
    print("QS REVERSE TIME:", timer)

    A = generator(100000)  # gen for heapsort, bubble and merge
    A2 = A[:]
    A3 = A[:]

    start = time.time()
    heapSort(A)
    stop = time.time()
    timer = stop - start
    print("HEAPSORT RANDOM TIME:", timer)

    B = []
    C = []
    B = list(A)
    C = list(reversed(A))

    start = time.time()
    heapSort(B)
    stop = time.time()
    timer = stop - start
    print("HEAPSORT SORTED TIME:", timer)

    start = time.time()
    heapSort(C)
    stop = time.time()
    timer = stop - start
    print("HEAPSORT REVERSE TIME:", timer)

    start = time.time()
    bubbleSort(A2)
    stop = time.time()
    timer = stop - start
    print("BUBBLE RANDOM TIME:", timer)

    B = []
    C = []
    B = list(A2)
    C = list(reversed(A2))

    start = time.time()
    bubbleSort(B)
    stop = time.time()
    timer = stop - start
    print("BUBBLE SORTED TIME:", timer)

    start = time.time()
    bubbleSort(C)
    stop = time.time()
    timer = stop - start
    print("BUBBLE REVERSE TIME:", timer)

    start = time.time()
    mergeSort(A3)
    stop = time.time()
    timer = stop - start
    print("MERGE RANDOM TIME:", timer)

    B = []
    C = []
    B = list(A3)
    print(A3)
    C = list(reversed(A3))

    start = time.time()
    mergeSort(B)
    stop = time.time()
    timer = stop - start
    print("MERGE SORTED TIME:", timer)

    start = time.time()
    mergeSort(C)
    stop = time.time()
    timer = stop - start
    print("MERGE REVERSE TIME:", timer)