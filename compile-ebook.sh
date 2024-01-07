#!/bin/bash
set -e

# pull the last version
git pull

# update lammps tutorials in case changes were made
git submodule update --remote

var1=$1

# convert the sphinx bibliography to ebook
if [[ "$var1" == "full" ]];
then
    cd converter/
    python3 sphinx-to-ebook.py
    cd ..
fi

cd tex/
# compile pdf
pdflatex lammps-tutorials-ebook.tex
# if full keyword is given, recompile pdf
if [[ "$var1" == "full" ]];
then
    pdflatex lammps-tutorials-ebook.tex
fi

mv lammps-tutorials-ebook.pdf _lammps-tutorials-ebook.pdf 
pdftk ../logo/first-page.pdf _lammps-tutorials-ebook.pdf  cat output lammps-tutorials-ebook.pdf
rm _lammps-tutorials-ebook.pdf
