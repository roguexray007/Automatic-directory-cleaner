#!/usr/bin/env python
import sys
import optparse
import subprocess

parser=optparse.OptionParser()
parser.add_option('-p','--path',dest='path',help='path of the directory')
(options,args)=parser.parse_args()

if options.path is None:
    options.path = input('Enter path of directory:')
#in case of mac use cmd2 (in mac ls -sh not displaying size in human readable format
# cmd2='find %s -exec du -a -h {} \;|sort -rh|grep ".*\.[a-zA-Z]"|uniq|head -n 10' % options.path  
#more optimized version for linux
cmd1='find %s -not -type d -exec ls -sh  {} \;|sort -rh|head -n 10' % options.path #for linux
proc=subprocess.call(cmd1,shell=True)



