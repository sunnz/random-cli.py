#!/usr/bin/env python3

import unittest
import random_cli
import string


class RandomCLITestCase(unittest.TestCase):
    def test_random_alphanumeric_string__len(self):
        result = random_cli.random_alphanumeric_string(10)
        self.assertEqual(
            len(result), 10, 'random_string does not return correct length.')

    def test_random_alphanumeric_string__alphanumeric(self):
        result = random_cli.random_alphanumeric_string(1)
        alphanumeric = string.ascii_letters + string.digits
        self.assertIn(result, alphanumeric)

    def test_random_hex_string__hex(self):
        result = random_cli.random_hex_string(1)
        self.assertIn(result, string.hexdigits)


if __name__ == '__main__':
    unittest.main()
