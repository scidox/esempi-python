#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest #modulo per fare test

class TestRearrange(unittest.TestCase):

    def test_basic(self):
        testcase="Lovalace, Ada"
        expected="Ada Lovalace"
        self.assertEqual(rearrange_name(testcase),expected)

    def test_empty(self):
        testcase=""
        expected=""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase="Hopper, Grace M."
        expected="Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase="Giorgio"
        expected="Giorgio"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
