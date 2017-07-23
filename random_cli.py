#!/usr/bin/env python3

import random
import string
import click


@click.command()
@click.argument('length', required=False, default=64)
def random_cli(length):
    click.echo(random_alphanumeric_string(length))


def random_alphanumeric_string(len):
    alphanumeric = string.ascii_letters + string.digits
    return random_string(len, alphanumeric)


def random_hex_string(len):
    return random_string(len, string.hexdigits)


def random_string(len, characters):
    result = ''
    while True:
        if len > 0:
            result += random.choice(characters)
            len -= 1
        else:
            return result


if __name__ == '__main__':
    random_cli()
