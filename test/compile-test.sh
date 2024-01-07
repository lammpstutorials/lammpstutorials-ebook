#!/bin/bash
set -e

jupyter-nbconvert --to script test-to-ebook.ipynb
    
python3 test-to-ebook.py

pdflatex test-ebook.tex
pdflatex test-ebook.tex

rm test-to-ebook.py