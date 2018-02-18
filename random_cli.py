#!/usr/bin/env python3

"""
a cli app that simply generates a random 64 character alphanumeric string.
"""

import secrets
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
        click.echo(random_printable_string(length))
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


def random_printable_string(len):
    printable = string.ascii_letters + string.digits + string.punctuation
    return random_string(len, printable)


def random_string(len, characters):
    result = ''
    while len > 0:
        result += secrets.choice(characters)
        len -= 1
    return result


if __name__ == '__main__':
    random_cli()
