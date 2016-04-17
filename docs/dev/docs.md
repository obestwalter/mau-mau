# Documentation building and hosting

## MkDocs and Github pages

### MkDocs

The documentation is generated with [MkDocs](http://www.mkdocs.org/) and it lives in [docs/](https://github.com/obestwalter/mau-mau/tree/master/docs/). The configuration is in [mkdocs.yml](https://github.com/obestwalter/mau-mau/blob/master/mkdocs.yml) ([YAML](https://en.wikipedia.org/wiki/YAML) format).

[Markdown](https://en.wikipedia.org/wiki/Markdown) is an easy to learn format that is the default on [Github](https://guides.github.com/features/mastering-markdown/) and [Stack Overflow](http://stackoverflow.com/editing-help). It is much easier on the eye than restructuredText - the established standard in the Python world. But it is also not as powerful. For more complex documentation [Sphinx](http://www.sphinx-doc.org) and [restructuredText](http://www.sphinx-doc.org/en/stable/rest.html) might be better suited.

### Github pages

Github offers to host the project documentation on [Github Pages](https://pages.github.com/). MkDocs has an inbuilt deploy functionality do push the documentation there. The pages are hosted as project homepage on [github.io](http://obestwalter.github.io/mau-mau/).

## Working on the documentation

When you work on the documentation you can start a local server:

    $ cd <path/to/your/clone>
    $ tox -e docs-auto
    
This prepares an environment and runs `mkdocs serve`. You can do it directly already. Using tox here is a bit of overkill, but serves to demonstrate, that you can use tox for automating and standardizing all kinds of development tasks. 

The documentation is now served on [localhost:8000](http://localhost:8000/) and changes are automatically detected and the website is reloaded.

Tidy up the build in case of big changes or problems:

    $ tox -e docs-clean
    
### Deploying the documentation

If you have push rights for the repository you can deploy the current documentation with:

    $ cd <path/to/your/clone>
    $ tox -e docs-deploy
