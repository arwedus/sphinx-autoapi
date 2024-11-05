templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = "pyisubmoduleinit"
copyright = "2015, readthedocs"
author = "readthedocs"
version = "0.1"
release = "0.1"
language = "en"
exclude_patterns = ["_build"]
pygments_style = "sphinx"
todo_include_todos = False
html_theme = "alabaster"
htmlhelp_basename = "pyisubmoduleinitdoc"
extensions = ["sphinx.ext.autodoc", "autoapi.extension"]
autoapi_dirs = ["example"]
