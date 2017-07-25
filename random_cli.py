#!/usr/bin/env python3

import random
import string
import click


@click.command()
@click.option(
    '--type',
    default='alphanumeric',
    help='type of characters to be generated.')
@click.argument('length', required=False, default=64)
def random_cli(type, length):
    if 'alphanumeric' == type:
        click.echo(random_alphanumeric_string(length))
    elif 'hex' == type:
        click.echo(random_hex_string(length))
    elif type in ['print', 'printable']:
        click.echo(random_string(length, string.printable))
    elif type in ['lower', 'lowercase']:
        click.echo(random_string(length, string.ascii_lowercase))
    elif type in ['upper', 'uppercase']:
        click.echo(random_string(length, string.ascii_uppercase))
    elif type in ['letter', 'letters', 'alpha']:
        click.echo(random_string(length, string.ascii_letters))


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
