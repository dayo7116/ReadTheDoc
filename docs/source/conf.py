# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MT CloudXR'
copyright = '2023, Moore Threads'
author = 'Moore Threads'

release = '0.1'
version = '0.1.0'

# -- General configuration
html_show_sourcelink = False
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'breathe',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

breathe_default_project = "MTCloudXR"
breathe_projects = { "MTCloudXR": "./../../doxygen/xml/" }
