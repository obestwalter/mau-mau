import itertools
import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    print("ERROR: At least Python 3.6 needed. You use Python %s" % sys.version)
    sys.exit(1)


def main():
    setup(
        name='mau-mau',
        author='Oliver Bestwalter',
        url='https://github.com/obestwalter/mau-mau',
        use_scm_version=True,
        setup_requires=['setuptools_scm', 'pytest-runner'],
        tests_require=['pytest'],
        packages=find_packages(),
        license='MIT',
        install_requires=['fire'],
        extras_require=generate_extras_require(),
        entry_points={'console_scripts': [
            'mau-mau = mau_mau.cli:main',
            'mau-mau-statistics = mau_mau.statistics:main',
        ]},
        classifiers=[
            'Programming Language :: Python :: 3.6',
            'Development Status :: 5 - Mature',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'License :: OSI Approved :: MIT License',
            'Topic :: Education',
            'Topic :: Games/Entertainment :: Turn Based Strategy',
        ]
    )


def generate_extras_require():
    extras = {
        ':sys_platform == "win32"': ['win_unicode_console'],
        'tests': ['tox', 'flake8', 'pytest', 'pytest-watch'],
        'docs': ['mkdocs', 'mkdocs-material']}
    extras.update(dict(all=list(itertools.chain(*extras.values()))))
    return extras


if __name__ == '__main__':
    main()
