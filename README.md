# Automatic-file-cleaner

1.largest_10_files.py --- using this u can get the top ten largest file size within the directory(recursively scan all folders 						     and files within that directory) u specify

2.cleaning.py --- example usage of this script -If there are 10 MP3 files, 3 word documents, 4 PDFs then in Documents Folder 				   three folders should be created with name MP3, DOC and PDF and all the files on the Desktop should be moved                   into these directories based on their file type or extension.
				  
I actually added option of specifying which directory u want to organise and where u want all the files to get organised..
Any file without extension will go into WITHOUT_EXT folder 

Additional feature--- if u want to exclude some extensions from being organised,just include that extension in the list named
		      		  exclude_ext

NOTE: for mac and linux user
in largest_10_files.py , for mac use cmd1 as ls -sh is not displaying size in human readable format in mac
and use optimised cmd 2 in linux.U can use cmd1 for linux also but cmd2 is optimised


REFER TO DEMO-RUN FOR MORE INSIGHT AND BETTER UNDERSTANDING
