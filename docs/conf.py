extensions = [
    'nbsphinx',
    'sphinxcontrib.rsvgconverter',  # for SVG->PDF conversion in LaTeX output
    'sphinx_gallery.load_style',  # load CSS for gallery (needs SG >= 0.6)
    'sphinx_last_updated_by_git',  # get "last updated" from Git
    'sphinx_codeautolink',  # automatic links from code to documentation
    'sphinx.ext.intersphinx',  # links to other Sphinx projects (e.g. NumPy)
]

# These projects are also used for the sphinx_codeautolink extension:
intersphinx_mapping = {
    'IPython': ('https://ipython.readthedocs.io/en/stable/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'python': ('https://docs.python.org/3/', None),
}

html_sourcelink_suffix = ''

mathjax3_config = {
    'tex': {'tags': 'ams', 'useLabelIds': True},
}

master_doc = 'index'

project = 'pyflink-docs'
author = 'Xingbo'
copyright = '2022, ' + author
html_show_copyright = False

html_title = project + ' version ' + '0.1'

if 'html_theme' not in globals():
    try:
        import insipid_sphinx_theme
    except ImportError:
        pass
    else:
        html_theme = 'insipid'
        html_copy_source = False
        html_permalinks_icon = '#'
