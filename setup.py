import itertools

from setuptools import setup


def get_extra_dependencies():
    extras = {
        'tests': ['tox', 'flake8', 'pytest', 'pytest-watch'],
        'docs': ['mkdocs']}
    extras.update(dict(all=list(itertools.chain(*extras.values()))))
    return extras


def main():
    setup(
        name='mau-mau',
        author='Oliver Bestwalter',
        url='https://github.com/obestwalter/mau-mau',
        # FIXME upload this to Pypi after all ...
        # use_scm_version=True,
        # setup_requires=['setuptools_scm'],
        version='4.0.1',  # tmp fix scm and github don't play together
        packages=['mau_mau'],
        license='MIT',
        install_requires=['win_unicode_console'],
        extras_require=get_extra_dependencies(),
        entry_points={'console_scripts': ['mau-mau = mau_mau.cli:main']},
    )


if __name__ == '__main__':
    main()
