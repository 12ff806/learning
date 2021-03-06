#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from mydict import Dict


# 测试类
class TestDict(unittest.TestCase):

    # 可以在单元测试中编写两个特殊的setUp()和tearDown()方法
    # 这两个方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print("setUp...")

    def tearDown(self):
        print("tearDown...")

    # 以test开头的方法就是测试方法
    # 不以test开头的方法不被认为是测试方法，测试的时候不会被执行
    def test_init(self):
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, Dict))

    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 这是最简单的运行单元测试的方式, 这样就可以把mydict_test.py当做正常的python脚本运行
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试: python3 -m unittest mydict_test
# 这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试
if __name__ == "__main__":
    unittest.main()


