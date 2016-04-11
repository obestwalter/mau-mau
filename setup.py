from setuptools import setup

setup(
    name='OOOMMM',
    version='1.0.0.dev0',
    url='https://github.com/obestwalter/mau-mau',
    author='Oliver Bestwalter',
    license='MIT',
    install_requires=[
        'commonmark==0.5.4',
        'recommonmark',
    ],
    packages=['mau_mau'],
    entry_points={'console_scripts': ['sim = mau_mau.cli:main']},
)
