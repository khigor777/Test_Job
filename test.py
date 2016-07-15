#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from home_work import *


class TestHomeWork(unittest.TestCase):

    def setUp(self):
        self.numbers = [55,77,1,-1]

        self.bit_count = [5,4,1,1]
        self.sort_list = [1, 2, 3]

    def test_bit_count(self):
        for item, b_count in zip(self.numbers, self.bit_count):
            self.assertEquals(get_bit_count(item), b_count)


    def test_binary_search(self):
        for i, z in zip([0, 1, 10, 5, 11], [-1, -1, -1, -1, -1]):
            self.assertEquals(binary_search(self.sort_list, i), z)


    def test_reverse_class(self):
        cla = ReverseClass()
        res = cla.reverse(self.sort_list)
        self.assertEquals(res[0], 3)

if __name__ == '__main__':
    unittest.main()