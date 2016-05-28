import itertools

from setuptools import setup


def get_extra_dependencies():
    extras = {
        'tests': ['tox', 'flake8', 'pytest', 'pytest-watch'],
        'docs': ['mkdocs', 'mkdocs-material']}
    extras.update(dict(all=list(itertools.chain(*extras.values()))))
    return extras


def main():
    setup(
        name='mau-mau',
        author='Oliver Bestwalter',
        url='https://github.com/obestwalter/mau-mau',
        use_scm_version=True,
        setup_requires=['setuptools_scm', 'pytest-runner'],
        tests_require=['pytest'],
        packages=['mau_mau'],
        license='MIT',
        install_requires=['win_unicode_console'],
        extras_require=get_extra_dependencies(),
        entry_points={'console_scripts': ['mau-mau = mau_mau.cli:main']},
    )


if __name__ == '__main__':
    main()
