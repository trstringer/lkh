from setuptools import setup

setup(
    name = 'lkh',
    version = '0.1.0',
    packages = ['lkh'],
    entry_points = {
        'console_scripts': [
            'lkh = lkh.__main__:main'
        ]
    })

