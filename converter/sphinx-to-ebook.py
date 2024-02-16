#!/usr/bin/env python
# coding: utf-8

import sys, os, git

current_path = os.getcwd()
git_repo = git.Repo(current_path, search_parent_directories=True)
git_path = git_repo.git.rev_parse("--show-toplevel")

from tutorialslist import tutorials, non_tutorials

sys.path.append(git_path + "/functions/")

from ReadRST import ReadRST
from WriteTEX import WriteTex
from FixDocument import FixDocument

for mode in ["light", "dark"]:

    folder = '/tex-'+mode+'/'

    if os.path.exists(git_path+folder+'converted_files') is False:
        os.mkdir(git_path+folder+'converted_files')

    for level in tutorials.keys():
        if os.path.exists(git_path+folder+'converted_files/'+level) is False:
            os.mkdir(git_path+folder+'converted_files/'+level)
        for tutorial in tutorials[level]:
            rst_path = git_path+'/lammpstutorials.github.io/docs/sphinx/source/tutorials/'+level+'/'
            rst_file_name = rst_path+tutorial+'.rst'
            tex_file_name = git_path+folder+'converted_files/'+level+'/'+tutorial+'.tex'   
            RST = ReadRST(rst_file_name, rst_path)
            RST.convert_file()
            assert len(RST.label_positions) == 1, """Careful, more than one label"""
            TEX = WriteTex(tex_file_name, RST, git_path, rst_path, mode)
            TEX.convert_file()
            FIX = FixDocument(tex_file_name)
            FIX.fix_document()

    if os.path.exists(git_path+folder+'converted_files/non-tutorials/') is False:
        os.mkdir(git_path+folder+'converted_files/non-tutorials/')

    for level in non_tutorials.keys():
        if os.path.exists(git_path+folder+'converted_files/'+level) is False:
            os.mkdir(git_path+folder+'converted_files/'+level)
        for tutorial in non_tutorials[level]:
            rst_path = git_path+'/lammpstutorials.github.io/docs/sphinx/source/tutorials/'+level+'/'
            rst_file_name = rst_path+tutorial+'.rst'
            tex_file_name = git_path+folder+'converted_files/'+level+'/'+tutorial+'.tex'   
            RST = ReadRST(rst_file_name, rst_path)
            RST.convert_file()
            assert len(RST.label_positions) == 1, """Careful, more than one label"""
            TEX = WriteTex(tex_file_name, RST, git_path, rst_path, mode, nonumber=True)
            TEX.convert_file()
            FIX = FixDocument(tex_file_name)
            FIX.fix_document()

    rst_path = git_path + '/lammpstutorials.github.io/docs/sphinx/source/non-tutorials/'
    rst_file_name = rst_path + 'before-you-start.rst'
    tex_file_name = git_path+folder+'converted_files/non-tutorials/before-you-start.tex'
    RST = ReadRST(rst_file_name, rst_path)
    RST.convert_file()
    assert len(RST.label_positions) == 1, """Careful, more than one label"""
    TEX = WriteTex(tex_file_name, RST, git_path, rst_path, mode, nonumber=True)
    TEX.convert_file()
    FIX = FixDocument(tex_file_name)
    FIX.fix_document()

    rst_path = git_path + '/lammpstutorials.github.io/docs/sphinx/source/non-tutorials/'
    rst_file_name = rst_path + 'solutions.rst'
    tex_file_name = git_path+folder+'converted_files/non-tutorials/solutions.tex'
    RST = ReadRST(rst_file_name, rst_path)
    RST.convert_file()
    assert len(RST.label_positions) == 1, """Careful, more than one label"""
    TEX = WriteTex(tex_file_name, RST, git_path, rst_path, mode, nonumber=True)
    TEX.convert_file()
    FIX = FixDocument(tex_file_name)
    FIX.fix_document()

    rst_path = git_path + '/lammpstutorials.github.io/docs/sphinx/source/non-tutorials/'
    rst_file_name = rst_path + 'glossary.rst'
    tex_file_name = git_path+folder+'converted_files/non-tutorials/glossary.tex'
    RST = ReadRST(rst_file_name, rst_path)
    RST.convert_file()
    assert len(RST.label_positions) == 1, """Careful, more than one label"""
    TEX = WriteTex(tex_file_name, RST, git_path, rst_path, mode, nonumber=True)
    TEX.convert_file()
    FIX = FixDocument(tex_file_name)
    FIX.fix_document()

    print("Compilation completed for", mode, "mode")