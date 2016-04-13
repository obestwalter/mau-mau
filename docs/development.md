# Development

## Documentation

The documentation is generated with [sphinx](http://www.sphinx-doc.org/) and the means to build it live in `docs`.

### Building the documentation

When you work on the documentation you can build it locally:

    $ cd <path/to/your/clone>/docs
    $ make html
    
results are in `<path/to/your/clone>/docs/_build`_

You can use `sphinx-autobuild` to have the docs rebuilt every time a project file changes. The results will be served on `http://localhost:8000`.

### Updating the online documentation

... happens automagically. When changes are pushed to Github a [webhook](http://read-the-docs.readthedocs.org/en/latest/webhooks.html#github) is triggered and the documentation is rebuilt. The [versioned](http://docs.readthedocs.org/en/latest/versions.html) result is hosted on [readthedocs](http://mau-mau.readthedocs.org) (likely where you are reading it right now :)).
