Template for the Read the Docs tutorial
=======================================

This GitHub template includes fictional Python library
with some basic Sphinx docs.

Read the tutorial here:

https://docs.readthedocs.io/en/stable/tutorial/


Setup (Use Git Bash)
1. python -m venv .venv
2. source .venv/Scripts/activate
3. python -m pip install sphinx
4. pip install sphinx_rtd_theme
5. pip install tools/breathe-4.35.0-py3-none-any.whl
6. download doxygen and install (add bin to Enviroment Variable), https://www.doxygen.nl/files/doxygen-1.9.8-setup.exe
7. cd ./doxygen && doxygen.exe
8. sphinx-build -M html docs/source/ docs/build