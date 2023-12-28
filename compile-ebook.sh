#!/bin/bash
set -e

var1=$1

# convert the sphinx bibliography to ebook
if [[ "$var1" == "full" ]];
then
    python3 sphinx-to-ebook.py
fi
# compile pdf
pdflatex lammps-tutorials-ebook.tex
# if full keyword is given, recompile pdf
if [[ "$var1" == "full" ]];
then
    pdflatex lammps-tutorials-ebook.tex
fi

mv lammps-tutorials-ebook.pdf _lammps-tutorials-ebook.pdf 
pdftk logo/first-page.pdf _lammps-tutorials-ebook.pdf  cat output lammps-tutorials-ebook.pdf
rm _lammps-tutorials-ebook.pdf
