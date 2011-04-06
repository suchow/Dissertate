#!/usr/bin/python

# build.py
#
# Created by Jordan Suchow.
# http://jwsu.ch/ow

import os
import sys

scripts_dir = '/scripts'
chapters_dir = '/chapters'
templates_dir = '/templates'

main_dir = sys.path[0].replace(scripts_dir,'')

# find the highest chapter number
chapter_list = os.listdir(main_dir + chapters_dir + '/')
chapter_list.remove('.DS_Store')
highest_chapter = max([int(chapter.replace('chapter', '').replace('.tex','')) for chapter in chapter_list])
	
# copy the template chapter to the chapters directory
os.chdir(main_dir + templates_dir)
high_chapter_string = str((highest_chapter))
new_chapter_string = str((highest_chapter + 1))
os.system('cp -R chapter.tex ../chapters/chapter' + new_chapter_string + '.tex')

# add the chapter to the thesis
os.system('sed -i -e \'s/' + high_chapter_string + '}/' + high_chapter_string + '}\\\include{chapters\/chapter' + new_chapter_string + '}/g\' ' + '../thesis.tex')
# exit terminal
os.system('exit')
