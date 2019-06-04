# encoding:utf-8

import json, unittest, re, time
from ddt import ddt, data, unpack, file_data
import itertools


@ddt
class case(unittest.TestCase):

    def test1(self):
        A = ['1', '2']
        B = ['a', 'b', 'c']

        for x in itertools.product(A, B):
            print(x)

    @data('1', '2', '3')
    def test2(self, keys):
        print(keys)

    @data(['a', 'b'], ['c', 'd'])
    @unpack
    def test3(self, values, keys):
        # print(values)
        print(keys)

    @file_data(r'E:\App_AutoTest\Public_file\test.json')
    def test4(self, values):
        print(values)


if __name__ == "__main__":
    unittest.main()
