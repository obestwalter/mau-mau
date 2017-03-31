# Getting started

!!! note
    Please replace `</path/to/your/clone>` with the actual path of your mau-mau repository clone on your computer.

To work on the code:

* [Fork](https://guides.github.com/activities/forking/) the repository
* [Clone](http://rogerdudler.github.io/git-guide/) the repository to `<path/to/your/clone>` (wherever that is).

... and install the code as editable in a [virtualenv](../guide/installation.md#in-a-virtualenv):

    $ <activate your virtualenv>
    $ cd <path/to/your/clone>
    $ pip install -e '.[all]'

The output looks like:

    Obtaining file:///</path/to/your/clone>
    Installing collected packages: mau-mau
      Running setup.py develop for mau-mau
    Successfully installed mau-mau

Make sure it is installed as editable:

    $ pip freeze

The output looks like (most packages removed from list):

    [...]
    -e git+git@github.com:obestwalter/mau-mau.git@e4031a17a5e08551317a321d7e74f9ca3b33e0b1#egg=mau_mau
    [...]
    win-unicode-console==0.4

The line starting with the `-e` indicates that mau-mau is installed as editable from github.

# Using vagrant

!!! TODO!
    Write about use of vagrant
