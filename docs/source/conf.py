# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MOST-def'
copyright = '2026, J. Craske'
author = 'J. Craske'

# -- general configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.bibtex'
]

bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'  # or 'plain', 'alpha', 'unsrtalpha'

templates_path = ['_templates']
exclude_patterns = []

myst_enable_extensions = ['html_image', 'colon_fence']
myst_html_img_enable = True
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    'logo': 'logo.png',
    'logo_name': False, # hides text title beneath logo
    'globaltoc_includehidden': True,
    'description': '',
    'github_user': 'most-def',
    'github_repo': 'most-def.github.io',
    'fixed_sidebar': True,
    "collapse_navigation": False,
    "navigation_depth": 3,
    "show_nav_level": 3
}

html_sidebars = {
    '**': [
        'about.html',
        'localtoc.html',
        'searchfield.html',
        'navigation.html',
    ]
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


