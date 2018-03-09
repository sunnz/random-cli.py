random-cli
==========

.. image:: https://img.shields.io/pypi/v/random_cli.svg
   :target: https://pypi.org/project/random_cli
.. image:: https://img.shields.io/badge/python-3.6%2B-blue.svg
.. image:: https://img.shields.io/github/license/sunnz/random-cli.py.svg
.. image:: https://img.shields.io/badge/readme%20style-standard-brightgreen.svg
   :target: https://github.com/RichardLitt/standard-readme

a cli app that simply generates 64 random alphanumeric characters.

for example::

    $ random
    vBDkKl1JqyeUu4n8ygrF0JflP6odhRnYSaxtND1dUSauNnUj7JDI9DHEYGs9FHhk

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
  3.6: <https://docs.python.org/3.6/library/secrets.html>.

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

usage: ``random [OPTIONS] [LENGTH]``

options::

    --type TEXT  alphanumeric (default), print, letters, lower, upper, hex
    --help       Show this message and exit.

``options`` and ``length`` is optional, default to 64 characters.

examples::

    $ random
    6aNaxiFpAtNCYAnyb7LjBCVS9ktQL2QNj1qDYUCvrUDctY4e4DFWMKz23CPmY0Of

    $ random 10
    8WsApVMknV

    $ random --type print
    0e;:e&%cghH-|/fo4L$tSrn&O'nOavWSfl"\1pW9Q4tO~}-eS2?C4N,PKv/XEX^?

    $ random --type letters
    UYUgcmuILkxiIsdHDRPOuCcxaOSIHryJHvTHRtOwPRnSqlsTIjTXheSVonhsPpWh

    $ random --type lower
    quthvsoxiqpipnigvzsjxugmbryczokqffyzmejhibktoitaszhtexgrptodgqnw

    $ random --type upper
    SAVGDFKDJRRSUFOGQOWYGEBKLPHMQXSSRCVLQHXZCAXRVJYOZERIMCPIINMZWDQK

    $ random --type hex
    85Bb8BaA8c3fbBcdbF3BAF7a7EeE0E8Aa2D22b87BA0EC315603A6cCaC27dBF9A

random_cli generates 64 random alphanumeric characters by default if no options
and length are given.

you should not get exactly the same results as above examples as random_cli
picks random characters from the given options. (you would be extremely lucky
if you do, as that equates to winning the lotto serveral times in a row!!)

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
<http://click.pocoo.org/6/python3/#python3-surrogates>.

development
-----------

setup virtualenv::

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt

from this point we assume that python refers to python 3 in virtualenv.

to run unit test (via python 3 pytest module)::

    python -m pytest --flake8 --cache-clear -v

to build command for testing (e.g. within virtualenv)::

    flit install

after which you can run it by running ``random`` in the terminal in virtualenv.
to rebuild simply run ``flit install`` again.

contribute
----------

you are very welcomed to open issues and/or submit pull requests on github:
<https://github.com/sunnz/random-cli.py>.

this project follows standard-readme specification:
<https://github.com/RichardLitt/standard-readme>.

if you find this project useful and would like to tip me over bitcoin, here's
my bitcoin tipping address: ``1P1v6k1Qr9Ad3fMLrtgj5PQjYLyZdjqLZP``.
100% optional, it would totally be an awesome encouragement, no matter what
the amount is! :)

licence
-------

isc (c) sunnz <https://github.com/sunnz>.
