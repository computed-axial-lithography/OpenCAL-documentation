# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "OpenCAL"
copyright = "2026, University of California, Berkeley"
author = "University of California, Berkeley"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx_design",
]

templates_path = ["_templates"]
# CentrifuCAL section temporarily removed from the build. Remove the line below to restore it.
exclude_patterns = ["step_by_step/centrifucal_stepbystep.rst"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['static']
html_logo = "static/oc_logo_new.png"
# html_logo = "static/opencal_logo_mediumblue_rbg.png"
html_theme_options = {
    "logo_only": True,
}

html_theme = "sphinx_rtd_theme"
# html_theme = "alabaster"
html_static_path = ["_static"]


html_css_files = [
    "custom.css",
]
