from setuptools import setup


def get_version():
    """see: https://www.python.org/dev/peps/pep-0396/"""
    with open('mau_mau/__init__.py') as f:
        return f.read().split('= ')[-1][1:-2]


def main():
    setup(
        name='OOOMMM',
        version=get_version(),
        author='Oliver Bestwalter',
        url='https://github.com/obestwalter/mau-mau',
        packages=['mau_mau'],
        license='MIT',
        entry_points={'console_scripts': ['sim = mau_mau.cli:main']},
        install_requires=[
            'pytest',
            'pytest-watch',
            'tox',
            'sphinx',
            'sphinx-autobuild',
            # version pinned: https://github.com/rtfd/recommonmark/issues/24
            'commonmark==0.5.4',
            'recommonmark',
        ],
    )


if __name__ == '__main__':
    main()
