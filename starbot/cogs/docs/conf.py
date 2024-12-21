# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = "Starfire Documentations"
copyright = "2023 - Present | Star"

# -- General configuration ---------------------------------------------------

extensions = ["myst_parser","sphinx_rtd_theme"]
templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store", ".venv", "venv"]

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_title = "Starfire Docs"

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "use_edit_page_button": True,
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "navbar_align": "content",
    "primary_sidebar_end": ["sidebar-ethical-ads"],
    "article_footer_items": ["last-updated", "edit-this-page"],
    "navigation_with_keys": True,
    "use_edit_page_button": True,
    "show_toc_level": 2,
    "navbar_links": [
        {"name": "Home", "url": "index"},
        {"name": "Features", "url": "features"},
        {"name": "Support", "url": "support"},
    ]
}

html_context = {
    "github_user": "LeDeathAmongst",
    "github_repo": "StarCogs/docs",
    "github_version": "master",  # or the branch name where your docs are located
}

# Source file suffix
source_suffix = ".md"

# Master document
master_doc = "index"
