# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MOST-def'
copyright = '2026, J. Craske'
author = 'J. Craske'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_theme_options = {
    'description': 'A short description of your research project',
    'github_user': 'your-org-name',
    'github_repo': 'your-org-name.github.io',
    'fixed_sidebar': True,
}

html_sidebars = {
    '**': [
        'about.html',
        'searchfield.html',
        'navigation.html',
    ]
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}



