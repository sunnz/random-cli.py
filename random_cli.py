#!/usr/bin/env python3

import random
import string
import click


@click.command()
@click.argument('length', required=False)
def random_cli(length):
    try:
        result = random_string(int(length))
    except:
        result = random_string()
    click.echo(result)


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
