#!/usr/bin/python3
'''function that finds a peak in a list of unsorted integers'''


def find_peak(list_of_integers):
    '''finds a peak'''
    li = list_of_integers
    l = len(li)
    if l == 0:
        return
    mid = l // 2
    if (mid == l - 1 or li[mid] >= li[mid + 1]) and (mid == 0 or li[mid] >= li[mid - 1]):
        return li[mid]
    if mid != l - 1 and li[mid + 1] > li[mid]:
        return find_peak(li[mid + 1:])
    return find_peak(li[:mid])
