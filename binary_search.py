import random
import time

length = 10000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
list1 = sorted(list(sorted_list))


def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search(l, target, low=0, high=None):
    if high is None:
        high = len(l) -1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)


if __name__ == '__main__':
    start = time.time()
    for target in list1:
        naive_search(list1, target)
    end = time.time()
    print('Naive Search Time: ', (end - start)/ length, 'seconds')

    start = time.time()
    for target in list1:
        binary_search(list1, target)
    end = time.time()
    print('Binary Search Time: ', (end - start)/ length, 'seconds')