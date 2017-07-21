#!/usr/bin/env python3

import unittest
import random_cli
import string


class RandomCLITestCase(unittest.TestCase):
    def test_len(self):
        result = random_cli.random_string(10)
        self.assertEqual(
            len(result), 10, 'random_string does not return correct length.')

    def test_alphanumeric(self):
        result = random_cli.random_string(1)
        alphanumeric = string.ascii_letters + string.digits
        self.assertIn(result, alphanumeric)


if __name__ == '__main__':
    unittest.main()
