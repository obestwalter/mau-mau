import itertools
from setuptools import setup, find_packages


def generate_extras_require():
    extras = {
        ':sys_platform == "win32"': ["win_unicode_console"],
        "test": ["flake8", "pytest", "pytest-watch"],
        "docs": ["mkdocs", "mkdocs-material"],
    }
    extras.update(dict(all=list(itertools.chain(*extras.values()))))
    return extras


setup(
    name="mau-mau",
    author="Oliver Bestwalter",
    url="https://github.com/obestwalter/mau-mau",
    license="MIT",
    use_scm_version=True,
    python_requires=">=3.6",
    setup_requires=["setuptools_scm", "pytest-runner"],
    install_requires=["fire"],
    extras_require=generate_extras_require(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        "console_scripts": [
            "mau-mau = mau_mau.cli:main",
            "mau-mau-statistics = mau_mau.statistics:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Development Status :: 5 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
        "Topic :: Education",
        "Topic :: Games/Entertainment :: Turn Based Strategy",
    ],
)
