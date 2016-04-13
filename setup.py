import itertools

from setuptools import setup


def get_version():
    """see: https://www.python.org/dev/peps/pep-0396/"""
    with open('mau_mau/__init__.py') as f:
        return f.read().split('= ')[-1][1:-2]


def get_extra_dependencies():
    extras = {
        'tests': ['tox', 'pytest', 'pytest-watch'],
        'docs': ['mkdocs']}
    extras.update(dict(all=list(itertools.chain(*extras.values()))))
    return extras


def main():
    setup(
        name='mau-mau',
        version=get_version(),
        author='Oliver Bestwalter',
        url='https://github.com/obestwalter/mau-mau',
        packages=['mau_mau'],
        license='MIT',
        install_requires=[],
        extras_require=get_extra_dependencies(),
        entry_points={'console_scripts': ['sim = mau_mau.cli:main']},
    )


if __name__ == '__main__':
    print(get_extra_dependencies())
    main()
