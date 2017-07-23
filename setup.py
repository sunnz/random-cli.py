from setuptools import setup

setup(
    name='random_cli',
    version='0.1.0',
    py_modules=['random_cli'],
    install_requires=[
        'Click>=5,<7',
    ],
    python_requires='>=3, <4',
    entry_points={
        'console_scripts': [
            'random=random_cli:random_cli',
        ],
    })
