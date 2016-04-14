# Get the sources

To work on the code:

* [fork](https://guides.github.com/activities/forking/) the code 
* [clone](http://rogerdudler.github.io/git-guide/) the repository to `<path/to/your/clone>` (wherever that is).

... and install the code as editable in a [virtualenv](https://docs.python.org/3/tutorial/venv.html):

    $ <activate your virtualenv>
    $ cd <path/to/your/clone>
    $ pip install -e '.[all]'

output like:

    Obtaining file:///</path/to/your/clone>
    Installing collected packages: mau-mau
      Running setup.py develop for mau-mau
    Successfully installed mau-mau
