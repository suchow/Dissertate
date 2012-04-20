#!/usr/bin/python

# build.py
#
# Created by Jordan Suchow.
# http://jwsu.ch/ow

import os
import sys

fileToTex = 'thesis'
texCommand = 'xelatex'
bibtexCommand = 'bibtex'

scripts_folder = '/scripts'
chapters_folder = '/chapters'

clear_junk_command = 'rm -f *.toc *.blg *.aux *.bbl *.lof *.out *.brf *.tex-e'

# generate all of the figures

# change directory, out of the 'scripts' folder
main_directory = sys.path[0].replace(scripts_folder,'')
os.chdir(main_directory)

# run the latex commands
for command in [texCommand, bibtexCommand, texCommand, texCommand]:
	os.system(command + ' ' + fileToTex)

# clean up the support files
os.system('mv ' + fileToTex + '.log .' + fileToTex + '.log')
os.system(clear_junk_command)

os.chdir(main_directory + chapters_folder + '/')
os.system(clear_junk_command)

# exit terminal
os.system('exit')
