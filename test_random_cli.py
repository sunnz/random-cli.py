#!/usr/bin/env python3

import random_cli
import string


class TestRandomCli:
    def test_random_alphanumeric_string__len(self):
        for i in range(10):
            result = random_cli.random_alphanumeric_string(64)
            assert len(result) == 64, \
                'random_alphanumeric_string does not return correct length.'

    def test_random_alphanumeric_string__alphanumeric(self):
        for i in range(10):
            alphanumeric = string.ascii_letters + string.digits
            result = random_cli.random_alphanumeric_string(64)
            for char in result:
                assert char in alphanumeric, \
                    "{} is not alphanumeric.".format(char)

    def test_random_hex_string__hex(self):
        for i in range(10):
            result = random_cli.random_hex_string(64)
            for char in result:
                assert char in string.hexdigits, \
                    "{} is not hexdigits".format(char)

    def test_random_printable_string__printable__len(self):
        for i in range(10):
            printable = string.ascii_letters + string.digits
            printable += string.punctuation
            result = random_cli.random_printable_string(64)
            assert len(result) == 64, \
                'random_printable_string does not return correct length.'
            for char in result:
                assert char in printable, "{} is not printable.".format(char)
