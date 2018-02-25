random-cli
==========

.. image:: https://img.shields.io/pypi/v/random_cli.svg
   :target: https://pypi.org/project/random_cli
.. image:: https://img.shields.io/github/license/sunnz/random-cli.py.svg
   :alt: isc licence

a cli app that simply generates a random 64 character alphanumeric string.

I am kind of sick and tired of not being able to generate a simple alphanumeric
random string for passwords or what not without relying on a web browser.

I really like something in the terminal so that it is kind of temporary yet I
can copy and paste it when I need it, and be able to simply close the terminal
window when I am done.

I find it surprising that there is no simple cli app to do this... I resort to
doing things like ``dd if=/dev/urandom count=1 | base64``, but this is not
ideal, it is a long command and just not very configurable. most of the time I
just want a simple alphanumeric string but base64 gives all kinds of things,
which is great for what it is, but not really intended for what I am doing most
of the time.

so here it is, a purpose built cli app just for generating random alphanumeric
strings.

security
--------

- random_cli is entirely hosted on the client machine, no internet connection
  is ever used after installation.

- randomness is provided by the python secrets module, introduced in python
  3.6: https://docs.python.org/3.6/library/secrets.html

  - the secrets module uses best source of cryptographic randomness provided
    by the operating system. on linux, that may be ``/dev/urandom``. they are
    suitable for managing data such as passwords, account authentication,
    security tokens, and related secrets.

- **disclaimer**: this project has not been security audited. while secrets
  module is cryptographically strong, you should do your own assessment if
  this project is suitable for your specific use case.

install
-------

random_cli requires python 3.6 or higher as random_cli uses the new
secrets module introduced in python 3.6.

you can install random_cli from pypi, or from source.

to install system wide from pypi with pip::

    sudo python3 -m pip install random_cli

I use "flit" to build and publish random_cli, so "flit" is required
if you want install from source::

    sudo python3 -m pip install flit

then you can build and install random_cli from source::

    git clone https://github.com/sunnz/random-cli.py random_cli
    cd random_cli
    flit install

that would install random_cli into your home directory.

to install system wide from source, instead of ``flit install``, run::

    sudo su
    FLIT_ROOT_INSTALL=1 flit install
    exit

usage
-----

example::

    random

gives you exactly 64 random alphanumeric characters.

you can specify the number of characters you want by passing a positive integer
to the command.

for example you can generate 10 characters instead by passing 10 to the
command::

    random 10

runtime error
-------------

if you see something like this error::

    Traceback (most recent call last):
      ...
    RuntimeError: Click will abort further execution because Python 3 was
      configured to use ASCII as encoding for the environment.
      ...

this can be fixed by exporting the locale to the encoding of choice. for
example, I am using australian english, so I would set my locale to
``en_AU.utf8`` by running the following::

    export LC_ALL=en_AU.utf8
    export LANG=en_AU.utf8

the set the locale permanently, this repo provides a script ``locale.sh``
under ``shell-scripts``. copy it to ``/etc/profile.d/locale.sh``.

see python 3 surrogates for more information:
http://click.pocoo.org/6/python3/#python3-surrogates

development
-----------

setup virtualenv::

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt

from this point we assume that python refers to python 3 in virtualenv.

to run unit test (via python 3 pytest module)::

    python -m pytest --flake8 -v

install pytest if you haven't installed from requirements.txt from above::

    python -m pip install pytest

to build command for testing (e.g. within virtualenv)::

    flit install

after which you can run it by running ``random`` in the terminal in virtualenv.
to rebuild simply run ``flit install`` again.
