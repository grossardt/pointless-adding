# pylint: disable=invalid-name
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("."))

import pointless_adding


# -- Project information -----------------------------------------------------
project = "Pointless Adding"
author = "André Großardt"

docs_url_prefix = "pointless"

# The short X.Y version
version = pointless_adding.__version__
# The full version, including alpha/beta/rc tags
release = pointless_adding.__version__

vers = version.split(".")
link_str = (
    f" https://github.com/grossardt/pointless-adding/blob/stable/{vers[0]}.{vers[1]}/docs/"
)

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx_design",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
]

# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------

autosummary_generate = True

# -----------------------------------------------------------------------------
# Autodoc
# -----------------------------------------------------------------------------
# Move type hints from signatures to the parameter descriptions (except in overload cases, where
# that's not possible).
autodoc_typehints = "description"
# Only add type hints from signature to description body if the parameter has documentation.  The
# return type is always added to the description (if in the signature).
autodoc_typehints_description_target = "documented_params"

#autodoc_default_options = {
#    "inherited-members": None,
#}

# Use both class and __init__ docstrings for the class concatenated
autoclass_content = "both"

language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["**site-packages", "_build", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "colorful"

# A boolean that decides whether module names are prepended to all object names
# (for object types where a “module” of some kind is defined), e.g. for
# py:function directives.
add_module_names = False

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_theme_options = {
    "logo": '',
    "github_user": 'grossardt',
    "github_repo": 'pointless-adding',
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "sparse": ("https://sparse.pydata.org/en/stable/", None),
}

html_context = {"analytics_enabled": True}
