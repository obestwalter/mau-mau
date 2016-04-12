#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

for p in ['mau_mau', 'tests']:
    sys.path.insert(0, os.path.abspath(p))


project = 'Mau Mau'
copyright = '2016, Oliver Bestwalter'
author = 'Oliver Bestwalter'
version = '1.1'
release = '1.1.0'
language = 'en'

###############################################################################

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = True

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

###############################################################################

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.4'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    # 'sphinx.ext.githubpages',
]

templates_path = ['_templates']
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst', '.md']

master_doc = 'index'


# either, you set today to some non-false value
# today = ''
# or today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_drafts']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

add_module_names = False

pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

###############################################################################

html_theme = 'alabaster'

# html_theme_options = {}

# html_theme_path = []

# html_title = 'Mau Mau v1.1.0'
html_short_title = 'Mau Mau'

html_logo = 'logo.jpg'
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
html_last_updated_fmt = ''

# html_use_smartypants = True
# html_sidebars = {}
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'MauMaudoc'

# ############################### MANPAGES ####################################

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'maumau', 'Mau Mau Documentation',
     [author], 1)
]

# man_show_urls = False
