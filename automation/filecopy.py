#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.1.2
# Author: Dinmukhamed Baizhanov, din@careerharbour.co.uk
# Credentials: This file is part of the Open Source Project at Career Harbour Ltd.

"""This is a file for the automatic copy files to git branches.

Copy this file to your desktop, run on desktop and not inside
git repo locally. Copy the file you wish to be pasted also to your desktop.
"""

import subprocess
from sys import argv

scriptname = argv

# State here only the path and not the name of the file to be copied.
# Close path with / throughout this file
print 'What is the absolute path to your copied file?'
fcpath = raw_input("> ")

# State here only the name and not the path of the file to be copied.
print 'What is the name of your copied file?'
fcname = raw_input('> ')

# Combines the full path with the name of the file to make it openable
fcfull = fcpath + fcname

# Opening the file
fccontentopen = open(fcfull)

# Reading the file to be copied.
fccontent = fccontentopen.read()

# File path to the local git repo, change this to suit your purposes.
print 'What is the absolutle path to your git repo locally?'
fppath = raw_input('> ')

# Name of the pasted file only. Not the path.
print 'What is the name of your pasted file?'
fpname = raw_input('> ')

# Putting all branches into a list to run the for loop later.
# You need to enter the branch names manually. Future updates
# will automate this.
branchname = ['test', 'dev', 'master', 'systems']

"""-----------Begin of copy-paste loop-----------"""

for bn in branchname:
    # Check out on a branch
    cmd = 'cd %s && git checkout %s' % (fppath, bn)
    subprocess.call(cmd, shell=True)

    # Combination of path and name for pasted file
    fpfull = fppath + fpname

    # Opens the file to be pasted into with writing access and creates
    # one if there is nothing there with the name fpname.
    fpcontent = open(fpfull, 'w')

    # Deletes the previous content in that file to be pasted into.
    fpcontent.truncate()

    # Pasting into the pasted file with the content of the copied file.
    fpcontent.write(fccontent)

    # Closes just the pasted file since if
    # you the copied file needs to remain opened for another loop.
    fpcontent.close()

    # Git add
    cmd2 = 'cd %s && git add .' % fppath
    subprocess.call(cmd2, shell=True)

    # Git commit
    cmd3 = ('cd %s && git commit -m ' +
            '"Updated %s on %s with %s"') % (fppath, fpname, bn, scriptname)
    subprocess.call(cmd3, shell=True)

    # Git push
    cmd4 = 'cd %s && git push' % fppath
    subprocess.call(cmd4, shell=True)

"""-----------End of copy-paste loop-----------"""

# Close the to be copied file.
fccontentopen.close()
