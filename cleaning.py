#!/usr/bin/env python
import sys
import optparse
import subprocess
import os
import shutil

# ls = subprocess.Popen(["ls", "-p", "."],  
#                       stdout=subprocess.PIPE,
#                      )

# # define the grep command
# grep = subprocess.Popen(["grep", "-v", "/$"],  
#                         stdin=ls.stdout,
#                         stdout=subprocess.PIPE,
#                         )

# # read from the end of the pipe (stdout)
# endOfPipe = grep.stdout

# # output the files line by line
# for line in endOfPipe:  
#     print (line.decode(),end=' ')

 
 #---------------------------------------------------------------------   
# new_dir='/Users/hardxray007/Desktop/new_dir' --sample test run path

parser=optparse.OptionParser()
parser.add_option('-s','--src',dest='path',help='path of the source directory to reorganise')
parser.add_option('-d','--dest',dest='new_dir',help='path of the destination directory where u want files to be reorganised')

(options,args)=parser.parse_args()

if options.path is None:
    options.path = input('Enter path of the source directory to reorganise:')

if options.new_dir is None:
    options.new_dir = input('Enter path of the destination directory where u want files to be reorganised')


if not os.path.exists(options.new_dir):
	os.makedirs(options.new_dir)

exclude_ext=['exe']		# u can specify the extensions to exclude (like for counterstrike we have .exe)

#path='/Users/hardxray007/Desktop' sample directory to reorganize
for root, dirs, files in os.walk(options.path):  
	if root!=options.path:
		continue
	files[:]=[f for f in files if not f.startswith('.')]
	for filename in files:
		print(filename)
		if "." not in filename:
			ext='.without_ext'
		else:
			ind=filename.rfind('.')+1
			ext=filename[ind:]
		if ext in exclude_ext:
			continue
		copy_dir_path=options.new_dir+'/'+ext.upper()
		if not os.path.exists(copy_dir_path):
			os.makedirs(copy_dir_path)
		shutil.move(root+'/'+filename,copy_dir_path+'/'+filename)
		#if u want to copy use shutil.copy instead of shutil.move
		#shutil.copy(root+'/'+filename,copy_dir_path+'/'+filename)
		
		 


