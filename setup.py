import itertools

from setuptools import setup, find_packages


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
        extras_require=generate_extras_require(),
        entry_points={'console_scripts': ['mau-mau = mau_mau.cli:main']},
        classifiers=[
            'Programming Language :: Python',
            'Development Status :: 5 - Mature',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
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
