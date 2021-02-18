# -*- coding: utf-8 -*-
#
# pythonguide documentation build configuration file, created by
# sphinx-quickstart on Wed Aug  4 22:51:11 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import datetime
import os
import sys
from pathlib import Path
import json
import dataladhandbook_support

# pull out author list from all-contributors spec
authors = [
    c['name'] for c in json.load(
        (Path(__file__).parent.parent / '.all-contributorsrc').open()).get(
            'contributors', [])
]
# make sure mih is last author
authors.append(authors.pop(authors.index('Michael Hanke')))


# autorunrecord setup (extension used to run and capture the output of
# examples)
autorunrecord_basedir = '/home/me'
# pre-crafted artificial environment to run the code examples in
autorunrecord_env = {
    # make everything talk in english
    'LANG': 'en_US.UTF-8',
    'LANGUAGE': 'en_US:en',
    'LC_CTYPE': 'en_US.UTF-8',
    # use very common shell
    'SHELL': '/bin/bash',
    # keep username extra short to save on line length
    'USER': 'me',
    'USERNAME': 'me',
    'HOME': autorunrecord_basedir,
    # earned a PhD in 1678 and taught mathematics at the University of Padua
    'GIT_AUTHOR_EMAIL': 'elena@example.net',
    'GIT_AUTHOR_NAME': 'Elena Piscopia',
    'HOST': 'padua',
    # maintain the PATH to keep all installed software functional
    'PATH': os.environ['PATH'],
    'GIT_EDITOR': 'vim',
    # prevent progress bars - makes for ugly runrecords. See https://github.com/datalad-handbook/book/issues/390
    'DATALAD_UI_PROGRESSBAR': 'none',
}
if 'CAST_DIR' in os.environ:
    autorunrecord_env['CAST_DIR'] = os.environ['CAST_DIR']
if 'VIRTUAL_ENV' in os.environ:
    # inherit venv, if there is any
    autorunrecord_env.update(VIRTUAL_ENV=os.environ['VIRTUAL_ENV'])


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('_themes'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinxcontrib.autorunrecord',
    'sphinxcontrib.rsvgconverter',
    'sphinxcontrib.plantuml',
    'dataladhandbook_support',
    'notfound.extension',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
current_year = datetime.datetime.now().year
project = u'datalad-handbook'
copyright = (u'2019-{} CC-BY-SA').format(current_year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = dataladhandbook_support.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    '_themes/*.rst',  # Excluded due to README.rst in _themes/
    '**/*admin', # useful for executing, but not showing code
]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'tango'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

manpages_url = 'http://docs.datalad.org/generated/man/{page}.html'

# numbered figures for better referencing
numfig = True
numfig_secnum_depth = 1

# convert quotes and dashes into to proper symbols
smartquotes = True

# Trim spaces before footnote references that are necessary for the reST parser
# to recognize the footnote, but do not look too nice in the output.
trim_footnote_reference_space = True

# -- Options for HTML output ---------------------------------------------------
html_baseurl = 'http://handbook.datalad.org/'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# more options: https://alabaster.readthedocs.io/en/latest/customization.html
html_theme_options = {
    'show_powered_by': False,
    'github_user': 'datalad-handbook',
    'github_repo': 'book',
    'github_banner': True,
    'show_related': True,
    # colors
    # "DataLad gray"
    'body_text': '#333',
    # this is a lighter variant of the "DataLad yellow"
    'note_bg': '#e2eacdff',
    # the real "DataLad dark gray"
    'note_border': '#333333ff',
    'fixed_sidebar': True,
    'show_relbar_bottom': True,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'The DataLad Handbook'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'index':    ['sidebarintro.html', 'sourcelink.html', 'searchbox.html', 'hacks.html'],
    '**':       ['sidebarlogo.html', 'localtoc.html', 'relations.html',
                 'sourcelink.html', 'searchbox.html', 'hacks.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'dataladhandbookdoc'


# -- Options for LaTeX output --------------------------------------------------
latex_engine = 'pdflatex'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  (
      'book_main',
      'dataladhandbook.tex',
      u'The DataLad Handbook',
      u'',
      'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '../artwork/logo.pdf'
latex_additional_files = [
    '../artwork/git_boxicon.pdf',
    '../artwork/more_boxicon.pdf',
    '../artwork/win_boxicon.pdf',
]

latex_toplevel_sectioning = 'part'
latex_show_pagerefs = True
latex_show_urls = 'footnote'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'figure_align': 'H',
    'sphinxsetup': r"""
verbatimwithframe=false,%
VerbatimColor={rgb}{1,1,1},%
VerbatimHighlightColor={named}{OldLace},%
TitleColor={named}{DarkGoldenrod},%
hintBorderColor={named}{LightCoral},%
attentionborder=3pt,%
attentionBorderColor={named}{Crimson},%
attentionBgColor={named}{FloralWhite},%
noteborder=2pt,%
noteBorderColor={named}{Orange},%
cautionborder=3pt,%
cautionBorderColor={named}{Cyan},%
cautionBgColor={named}{LightCyan}%
""",
    'maketitle': r"""
\begin{titlepage}
\raggedleft
\rule{1pt}{\textheight}
\hspace{0.05\textwidth}
\parbox[b]{0.75\textwidth}{
\includegraphics[width=0.75\textwidth]{logo.pdf}\\
{\Huge\textbf{The handbook}}\hfill{\footnotesize %s}\\[1\baselineskip]
{\Large Introduction \textbullet\ Advanced topics \textbullet\ Use cases}\\[2\baselineskip]
{\Large\textsc{Adina~Wagner \& Michael~Hanke}\\[1\baselineskip]
{\small \textit{with}}\\[1\baselineskip]
{
\raggedright
%s\\
}}
}
\end{titlepage}
""" % (
        release,
        ', '.join('\\mbox{%s}' % a for a in authors[1:-1]),
    ),
    'extraclassoptions': 'openany,twoside',
    'fncychap': r'\usepackage[Bjarne]{fncychap}',
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',
    'preamble': r"""
\usepackage[labelfont=bf,singlelinecheck=false]{caption}
\renewcommand{\sphinxstyletheadfamily}{\bfseries}
\usepackage{charter}
\usepackage[defaultsans]{lato}
\usepackage{inconsolata}

% nice boxes
\usepackage[skins,breakable,many]{tcolorbox}
\tcbset{breakable}
\tcbset{drop lifted shadow}
\tcbset{sharp corners}
\tcbset{fonttitle=\bfseries}

\tcbset{%
ribbon win/.style={overlay={
  \begin{scope}[shift={([xshift=-5mm,yshift=-3mm]frame.north west)}]
    \path(0,0) node[inner sep=0] {\includegraphics{win_boxicon}};
  \end{scope}}}
}
\tcbset{%
ribbon git/.style={overlay={
  \begin{scope}[shift={([xshift=-5mm,yshift=-3mm]frame.north west)}]
    \path(0,0) node[inner sep=0] {\includegraphics{git_boxicon}};
  \end{scope}}}
}
\tcbset{%
ribbon more/.style={overlay={
  \begin{scope}[shift={([xshift=-5mm,yshift=-3mm]frame.north west)}]
    \path(0,0) node[inner sep=0] {\includegraphics{more_boxicon}};
  \end{scope}}}
}

\newtcolorbox[%
  auto counter,
  number within=chapter,
  list inside=windowsworkarounds]{windowsworkaround}[2][]{%
    enhanced, ribbon win, title={#2},
    coltitle=dataladgray,
    colbacktitle=windowsgreen,
    colframe=windowsgreen!70!black, #1
}
\newtcolorbox[%
  auto counter,
  number within=chapter,
  list inside=gitusernotes]{gitusernote}[2][]{%
    enhanced, ribbon git, title={#2},
    coltitle=dataladgray,
    colbacktitle=dataladblue,
    colframe=dataladblue!70!black, #1
}
\newtcolorbox[
  auto counter,
  number within=chapter,
  list inside=findoutmores]{findoutmore}[2][]{%
    enhanced, ribbon more, title={#2},
    coltitle=dataladgray,
    colbacktitle=dataladyellow,
    colframe=dataladyellow!70!black, #1
}

\setcounter{tocdepth}{1}
\usepackage{xcolor}
\definecolor{dataladyellow}{HTML}{FFA200}
\definecolor{dataladblue}{HTML}{7FD5FF}
\definecolor{dataladgray}{HTML}{333333}
\definecolor{windowsblue}{HTML}{126e12}
\definecolor{windowsgreen}{HTML}{66CC33}
\definecolor{windowsyellow}{HTML}{FFCC00}
\setcounter{secnumdepth}{1}
\newsavebox{\selvestebox}
\newenvironment{colbox}[1]
  {\newcommand\colboxcolor{#1}%
   \begin{lrbox}{\selvestebox}%
   \begin{minipage}{\dimexpr\columnwidth-2\fboxsep\relax}}
  {\end{minipage}\end{lrbox}%
   \begin{center}
   \colorbox[HTML]{\colboxcolor}{\usebox{\selvestebox}}
   \end{center}}
\newcommand*\ruleline[1]{\par\noindent\raisebox{.8ex}{\makebox[\linewidth]{\hrulefill\hspace{1ex}\raisebox{-.8ex}{#1}\hspace{1ex}\hrulefill}}}
\newenvironment{colortext}{\color{orange}}{\ignorespacesafterend}


\numberwithin{table}{chapter}
\numberwithin{figure}{chapter}
""",
}

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'dataladhandbook', u'The DataLad Handbook',
     [u'all'], 1)
]


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'dataladhandbook'
epub_author = u'all'
epub_publisher = u'all'
epub_copyright = u'2019–{}, all'.format(current_year)

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = [
    ('search.html', 'Search'),
]

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

todo_include_todos = False

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

plantuml_output_format = 'svg'
plantuml_latex_output_format = 'pdf'


def setup(app):
    app.add_stylesheet('custom.css')
    app.add_config_value('internal', '', 'env')
