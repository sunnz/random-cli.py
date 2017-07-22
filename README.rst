random-cli
----------

a cli app that simply generates a random 64 character alphanumeric string.

i am kind of sick and tired of not being able to generate a simple alphanumeric
random string for passwords or what not without relying on a web browser.

i really like something in the terminal so that it is kind of temporary yet i
can copy and paste it when i need it, and be able to simply close the terminal
window when i am done.

i find it surprising that there is no simple cli app to do this... i resort to
doing things like ``dd if=/dev/urandom count=1 | base64``, but this is not
ideal, it is a long command and just not very configurable. most of the time i
just want a simple alphanumeric string but base64 gives all kinds of things,
which is great for what it is, but not really intended for what i am doing most
of the time.

so here it is, a purpose built cli app just for generating random alphanumeric
strings.

example usage::

    ./random_cli.py

to run unit test (via python3 unittest module)::

    python3 -m unittest -v
