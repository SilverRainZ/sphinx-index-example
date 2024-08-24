# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Index Example'
copyright = '2024, Shengyu Zhang'
author = 'Shengyu Zhang'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

from typing import Iterable
from sphinx.domains import Index, IndexEntry
from sphinx.application import Sphinx

class MyIndex(Index):
   name = 'metavar'
   localname = 'Meta Variable Reference Index'
   shortname = 'references'

   def generate(
       self, docnames: Iterable[str] | None = None
   ) -> tuple[list[tuple[str, list[IndexEntry]]], bool]:
       idx1 = IndexEntry('foo', 0, 'docname', 'anchor', 'extra', 'qualifier', 'desc')
       idx2 = IndexEntry('bar', 0, 'docname', 'anchor', 'extra', 'qualifier', 'desc')
       idx3 = IndexEntry('baz', 1, 'docname', 'anchor', 'extra', 'qualifier', 'desc')
       idx4 = IndexEntry('qux', 2, 'docname', 'anchor', 'extra', 'qualifier', 'desc')
       idx5 = IndexEntry('quux', 1, 'docname', 'anchor', 'extra', 'qualifier', 'desc')

       return (
           # entry list
           [ 
               ("letter1", [idx1, idx2]),
               ("letter2", [idx3, idx4, idx5]),
           ],
           # collapse
           False,
       )


def setup(app: Sphinx):
    app.add_index_to_domain('std', MyIndex)
