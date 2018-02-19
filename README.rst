random-cli
==========

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

install
-------

random_cli requires python 3.6 or higher as random_cli uses the new
secrets module introduced in python 3.6.

you can install random_cli with pip or from source. (or both?)

pip::

    sudo python3 -m pip install random_cli

from source::

    cd /path/to/repo
    sudo python3 -m pip install .

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

development
-----------

setup virtualenv::

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

from this point we assume that python refers to python 3 in virtualenv.

to run unit test (via python 3 pytest module)::

    python -m pytest --flake8 -v

install pytest if you haven't installed from requirements.txt from above::

    python -m pip install pytest

to build command for testing (e.g. within virtualenv)::

    python setup.py develop

after which you can run it by running ``random`` in the terminal in virtualenv.
