#!/usr/bin/python
# -*- coding: utf-8 -*-

# Version 0.1.6
# Author: Dinmukhamed Baizhanov, din@careerharbour.co.uk
# Credentials: This file is part of the Open Source Project at Career Harbour Ltd.

"""This script is for the automatic and repetitive backup of git branches

You need to copy paste this code to a folder outside
the local git repo, then run in terminal python backup.py
Follow the input prompts in the terminal and specify the paths
of git repo and the location of backup.

You still need to specify manually all the branch names in the list:
branchname for all the local git branches you wish to back up.

The directory on your backup disk does not need to be created
separately prior to running this script.
"""

import subprocess
import time
import datetime
from sys import argv

# storing the name of this very script that has been called.
scriptname = argv

# This is for dynamic backup with custom path
# State the absolute path with / at the end
print 'What is the absolute path to your backup directory?'
fcpath = raw_input('> ')
print 'What is the absolutle path to your local git repo?'
fppath = raw_input('> ')

# This is for a faster backup experience with pre-defined paths
# Use for convenience, not for portability, uncomment for usage
# and comment the input lines above.
#fcpath = '/path/to/your/backup/disk/'
#fppath = '/users/your/path/to/git/repo/'

# Putting all branches into a list to run a for loop
branchname = ['dev', 'master', 'systems', 'test']

#  Making a new directory with the current date on backup disk
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%d.%m.%Y.%H.%M.%S')
full_fcpath = fcpath + st + '/'
makedir = 'mkdir %s' % full_fcpath
subprocess.call(makedir, shell=True)

for bn in branchname:

    # This will checkout to each branch in the list branchname
    cmd = 'cd %s && git checkout %s' % (fppath, bn)
    subprocess.call(cmd, shell=True)

    # This makes a separate subfolder in the backup path
    # for each git branch
    cmd2 = 'cd %s && mkdir %s' % (full_fcpath, bn)
    subprocess.call(cmd2, shell=True)

    # Creating a new path to the correct backup location
    backuppath = full_fcpath + bn

    # Copies all files under the fppath dir
    # to the backup location.
    cmd3 = 'cp -r %s %s' % (fppath, backuppath)
    subprocess.call(cmd3, shell=True)

# Optional: Bare git repo backup of your entire local git repo.
# Uncomment for usage. cmd_b1 should be pointing to the directory
# immediately above the local git repo to be backed up.
# Also change nameofyourgitrepo to the actual name of your git repo.
#cmd_b1 = 'cd /path/to/dir/just/above/gitrepo/'
#cmd_b2 = 'git clone --bare nameofyourgitrepo nameofyourgitrepo%s.git' % st
#cmd_b3 = 'mv nameofyourgitrepo%s.git %s' % (st, full_fcpath)
#subprocess.call(cmd_b1 + ' && ' + cmd_b2 + ' && ' + cmd_b3, shell=True)
