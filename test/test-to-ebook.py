#!/usr/bin/env python
# coding: utf-8

import sys, os, git

current_path = os.getcwd()
git_repo = git.Repo(current_path, search_parent_directories=True)
git_path = git_repo.git.rev_parse("--show-toplevel")

from testslist import tests

sys.path.append(git_path + "/functions/")

from ReadRST import ReadRST
from WriteTEX import WriteTex
from FixDocument import FixDocument

if os.path.exists(git_path+'/test/tex/converted_files') is False:
    os.mkdir(git_path+'/test/tex/converted_files')

for level in tests.keys():
    if os.path.exists(git_path+'/test/tex/converted_files/'+level) is False:
        os.mkdir(git_path+'/test/tex/converted_files/'+level)
    for tutorial in tests[level]:
        print(level, "tutorial", tutorial)
        print("-----------------------------------------")
        rst_file_name = git_path+'/test/rst/'+level+'/'+tutorial+'.rst'
        tex_file_name = git_path+'/test/tex/converted_files/'+level+'/'+tutorial+'.tex'   
        RST = ReadRST(rst_file_name)
        RST.convert_file()




# assert len(RST.label_positions) == 1, """Careful, more than one label"""
#TEX = WriteTex(tex_file_name, RST, git_path)
#TEX.convert_file()
#FIX = FixDocument(tex_file_name)
#FIX.fix_document()
