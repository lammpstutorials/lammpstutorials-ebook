#!/bin/bash
set -e
    
python3 test-to-ebook.py

pdflatex test-ebook.tex
pdflatex test-ebook.tex
