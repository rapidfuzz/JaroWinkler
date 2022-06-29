#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest

from jarowinkler import jarowinkler_similarity

class JaroWinklerTest(unittest.TestCase):

    def _jaro_winkler_similarity(self, s1, s2, result):
        self.assertAlmostEqual(jarowinkler_similarity(s1, s2), result, places=4)
        self.assertAlmostEqual(jarowinkler_similarity(s2, s1), result, places=4)

    def test_hash_special_case(self):
        self._jaro_winkler_similarity([0, -1], [0, -2], 0.66666)

    def test_edge_case_lengths(self):
        self._jaro_winkler_similarity('', '', 0)
        self._jaro_winkler_similarity('0', '0', 1)
        self._jaro_winkler_similarity('00', '00', 1)
        self._jaro_winkler_similarity('0', '00', 0.85)

        self._jaro_winkler_similarity('0'*65, '0'*65, 1)
        self._jaro_winkler_similarity('0'*64, '0'*65, 0.9969)
        self._jaro_winkler_similarity('0'*63, '0'*65, 0.9938)

        s1='10000000000000000000000000000000000000000000000000000000000000020'
        s2='00000000000000000000000000000000000000000000000000000000000000000'
        self._jaro_winkler_similarity(s1, s2, 0.97948)

        s1 = '00000000000000100000000000000000000000010000000000000000000000000'
        s2 = '0000000000000000000000000000000000000000000000000000000000000000000000000000001'
        self._jaro_winkler_similarity(s2, s1, 0.95333)

        s1 = '00000000000000000000000000000000000000000000000000000000000000000'
        s2 = '01000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        self._jaro_winkler_similarity(s2, s1, 0.85234)


if __name__ == '__main__':
    unittest.main()
