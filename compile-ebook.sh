#!/bin/bash
set -e

# pull the last version
git pull

# update lammps tutorials in case changes were made
git submodule update --remote

cd converter/
python3 sphinx-to-ebook.py
cd ..

# copy bib file (careful with special caracters)
#cp lammpstutorials.github.io/docs/sphinx/source/journal-article.bib tex/bibliography.bib

cd tex/
# compile pdf
pdflatex lammps-tutorials-ebook.tex
bibtex lammps-tutorials-ebook
pdflatex lammps-tutorials-ebook.tex
pdflatex lammps-tutorials-ebook.tex

# replace cover
mv lammps-tutorials-ebook.pdf _lammps-tutorials-ebook.pdf 
pdftk ../logo/first-page.pdf _lammps-tutorials-ebook.pdf cat output lammps-tutorials-ebook.pdf
rm _lammps-tutorials-ebook.pdf
cd ..