#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sphinx_rtd_theme
from datetime import datetime

import mau_mau

project = 'Mau Mau'
author = 'Oliver Bestwalter'
language = 'en'

_started = 2016
_cur = datetime.now().year
_range = '%s%s' % (_started, '' if _started == _cur else _cur)
copyright = '%s, Oliver Bestwalter' % (_range)

version = mau_mau.__version__[:-2]
release = mau_mau.__version__

# DEBUG SETTINGS ##############################################################
keep_warnings = True
todo_include_todos = True
# BASIC SETTINGS ##############################################################

needs_sphinx = '1.3'
master_doc = 'index'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]
templates_path = ['_templates']
# Using Markdown (additionally) is possible already but very limited
# version pinned: https://github.com/rtfd/recommonmark/issues/24
# pip install 'commonmark==0.5.4' recommonmark
source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}
source_suffix = ['.rst', '.md']
# today_fmt = '%B %d, %Y'
exclude_patterns = ['_drafts']
# add_function_parentheses = True
add_module_names = False
# modindex_common_prefix = []

# HTML SPECIFIC SETTINGD ######################################################

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# html_theme_options = {}
html_title = 'Mau Mau %s' % (version)
html_short_title = 'Mau Mau'
html_static_path = ['_static']
html_logo = '_static/logo_small.jpg'
html_last_updated_fmt = ''
htmlhelp_basename = 'Mau_Mau_doc'
