# Getting started

!!! note 
    Please replace `</path/to/your/clone>` with the actual path of your mau-mau repository clone on your computer.

To work on the code:

* [Fork](https://guides.github.com/activities/forking/) the code 
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
