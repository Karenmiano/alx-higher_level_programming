#!/usr/bin/python3
"""Contains one function find_peak."""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    if list_of_integers is None or list_of_integers == []:
        return None
    length = len(list_of_integers)
    peak_index = findpeak(list_of_integers, length)
    return list_of_integers[peak_index]


def findpeak(arr, n):
    """finds peak index"""
    low = 0
    high = n - 1

    while (low <= high):
        mid = (low + high) >> 1
        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
            break
        if (mid > 0 and arr[mid - 1] > arr[mid]):
            high = mid - 1
        else:
            low = mid + 1

    return mid
