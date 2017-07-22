#!/usr/bin/env python3

import random
import string
import click


@click.command()
@click.argument('length', required=False, default=64)
def random_cli(length):
    click.echo(random_string(int(length)))


def random_string(len=64):
    result = ''
    while True:
        if len > 0:
            alphanumeric = string.ascii_letters + string.digits
            result += random.choice(alphanumeric)
            len -= 1
        else:
            return result


if __name__ == '__main__':
    random_cli()
