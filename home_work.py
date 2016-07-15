#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
sys.maxint
The largest positive integer supported by Python’s regular integer type.
This is at least 2**31-1. The largest negative integer is -maxint-1 —
the asymmetry results from the use of 2’s complement binary arithmetic.
'''


def get_bit_count(number):
    '''
    Написать функцию “int getBitCount(int number)”,
    результатом которой будет количество ненулевых битов в числе.
    '''
    return bin(number).count('1')


def binary_search(a, x, lo=0, hi=None):
    '''
    Функция бинарного поиска в отсортированном массиве int[]. Без рекурсии.
    '''
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            return mid
    return -1


class ReverseClass(list):
    '''
    Написать функцию переворота односвязного списка.
     Реализовать собственный класс списка. Без рекурсии.
    '''
    def reverse(self, arr):
        result = []
        count = -1
        for item in arr:
            result.append(arr[count])
            count -= 1
        return result