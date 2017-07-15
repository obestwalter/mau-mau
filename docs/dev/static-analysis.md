# Static code analysis

## Flake8

[Flake8](https://pypi.python.org/pypi/flake8) is a collection of tools that analyze the code without running it. This can be understood as a first line of defense and you learn about style and complexity problems you might have in your code.

Run flake8 analysis:

    $ cd <path/to/your/clone>
    $ flake8 mau_mau/ tests/ --show-source

If flake8 is happy it won't produce any output. If not, it looks ike this:


    mau_mau/cli.py:39:80: E501 line too long (84 > 79 characters)
    ####################################################################################
                                                                                   ^
    mau_mau/cli.py:41:1: E302 expected 2 blank lines, found 1
    def simple_parse_args(argv):
    ^

## Quantified Code [![Code Issues](https://www.quantifiedcode.com/api/v1/project/663c550f107844aa842b4ce5e02883c4/badge.svg)](https://www.quantifiedcode.com/app/project/663c550f107844aa842b4ce5e02883c4)

**NOTE** sadly quantified code is shutting down its services at some point in 2017 so this might not work anymore. A potential similar alternative is https://coala.io - I am looking into this at the moment and might add it to the project later.

Quantified Code offers static code analysis as a webservice that connects to your Github repository. It is an interesting new approach and can teach you a lot about the code you write. It is not just pointing out problems, it tries to educate about the reasoning behind them and even helps to fix the problems. Definitely [worth a look](https://www.quantifiedcode.com/app/project/663c550f107844aa842b4ce5e02883c4).
