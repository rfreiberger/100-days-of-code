#!/usr/bin/env python3
# Author: Robert Freiberger
# Date : 2/11/2019
# Title: dbprep.py
# Notes: Simple script to take a CSV from Google Sheets and 
#        format this into a handy command list of actions
# repo:  https://github.com/rfreiberger/100-days-of-code
# Update: please note this is a script developed for my work but has been 
#         scrubbed of any important data, it's listed here as an example
#         of my Python work. 

import argparse
import csv
from datetime import datetime
import os 
import subprocess
import sys
import tarfile 

## Variables ##
# Phab repo link (note this should not change any time soon)
phab_repo = "<enter your repo here>"

def arguments():
    """Arguments for the file name and region"""

    file_name = ""
    region    = ""
    branch    = ""
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', action='store',
                        dest='file_name_value',
                        help='Name of the file to read')

    parser.add_argument('-r', action='store',
                        dest='region_value',
                        help='Name of the region to filter')

    parser.add_argument('-b', action='store',
                        dest='git_branch',
                        help='Name of the branch we will clone')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()
    # print(type(results))
    print('Welcome to dbprep.py')
    print("Below are the values we have received and will create the deploy files")
    print('file_name_value  = {!r}'.format(results.file_name_value))
    print('region_value     = {!r}'.format(results.region_value))
    print('git_branch       = {!r}'.format(results.git_branch))

    if not results.file_name_value:
        # no file name was given
        print("Please enter a file name value")
        print("Example: ./dbprep.py -f <file> -r [us,eu,la] -b <branch>")
        sys.exit()
    else:
        # file name was given
        file_name = results.file_name_value.lower()
    
    if not results.region_value:
        # no region was given
        print("Please enter a region value")
        print("Example: ./dbprep.py -f <file> -r [us,eu,la] -b <branch>")
        sys.exit()
    else:
        # region was given
        region = results.region_value.lower()

    if not results.git_branch:
        # no branch was given
        print("Please enter a git branch")
        print("Example: ./dbprep.py -f <file> -r [us,eu,la] -b <branch>")
        sys.exit()
    else:
        # note, git branches are case sensitive
        branch = results.git_branch
    
    return file_name, region, branch

def system_command(command):
    """Function to run a system command and return stdout"""

    try:
        syscommand = subprocess.run(
            command,
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as err:
        print('Error: ', err)
        sys.exit()
    else:
        print('Returncode: ', syscommand.check_returncode)
        syscommand_stdout = syscommand.stdout.decode("utf-8")
        return syscommand_stdout

def system_command_cwd(command, cwd_value):
    """Function to run a system command and return stdout with cwd option"""

    try:
        syscommand = subprocess.run(
            command,
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            cwd=cwd_value
        )
    except subprocess.CalledProcessError as err:
        print('Error: ', err)
        sys.exit()
    else:
        print('Returncode: ', syscommand.check_returncode)
        syscommand_stdout = syscommand.stdout.decode("utf-8")
        return syscommand_stdout 

def read_file(filename):
    """Read the file from input"""

    try:
        filename_csv = csv.DictReader(open(filename))
        return(filename_csv)
    except IOError:
        print("Could not read file: " + str(filename))
        sys.exit() 

def filter_region(file_dict, region):
    """Find the filter based upon the region arg"""

    if region == "us":
        filter_row = "Run in US?"
        return filter_row
    elif region == "eu":
        filter_row = "Run in EU?"
        return filter_row
    elif region == "la":
        filter_row = "Run in LA?"
        return filter_row
    else:
        print("Unknown region, please select us/eu/la")
        sys.exit()

def filter_sheet(dict_sheet, region_filter):
    """Filter the dictionary sheet with the region filter"""

    filter_results = []
    for row in dict_sheet:
        if row[region_filter] == "YES":
            filter_results.append("./server/" + row['Migrations'])
    
    return filter_results

def check_repo(repo, branch):
    """Check the status of the repo if it exists and pull, else it would clone"""

    if os.path.exists("./server") is True:
        # Checking if the branch is correct

        sys_command           = "git branch | awk '{print $2}'"
        sys_cwd               = "./server/."
        git_branch_result     = system_command_cwd(sys_command, sys_cwd)

        if git_branch_result  == branch:
            # if correct, check if current

            sys_command       = "git pull"
            sys_cwd           = "./server/."
            git_pull_result   = system_command_cwd(sys_command, sys_cwd)

            return True
  
        else:
            # if not correct branch, git checkout 

            sys_command         = "git checkout " + str(branch)
            sys_cwd             = "./server/."
            git_checkout_result = system_command_cwd(sys_command, sys_cwd)

            return True
        
    else:
        # else git clone correct branch 

        print("We did not find the server repo locally, running git clone...")
        sys_command      = "git clone " + str(phab_repo) + " -b " + str(branch)
        git_clone_result = system_command(sys_command)

        return True 
            
def clone_repo(repo,branch):
    """Cloning the branch in Phabricator locally"""

    print("We did not find the server repo locally, running git clone...")
    sys_command      = "git clone " + str(phab_repo) + " -b " + str(branch)
    git_clone_result = system_command(sys_command)

    return True 

def create_tar(migration_list):
    """This will create the tar file with the list of files"""

    time_stamp = (datetime.now().isoformat(timespec='minutes'))
    sys_command   = "whoami"
    whoami_result = system_command(sys_command)
    tar_file_name = str(whoami_result.strip()) + "-" + str(time_stamp.strip()) + ".tar"

    try:
        with tarfile.open(tar_file_name, mode='w') as out:
            for files in migration_list:
                out.add(files)
    except tarfile.FileNotFoundError as err:
        print('Error: ', err)
        sys.exit()
    else:
        print("Tar file has been created: " + str(tar_file_name))

def main():
    """Migration script to help prep the workflow of db migrations"""

    file_name, region, git_branch = arguments()

    file_dict = read_file(file_name)

    region_filter = filter_region(file_dict,region)

    migration_list = []
    migration_list = filter_sheet(file_dict,region_filter)

    check_repo(phab_repo,git_branch)

    create_tar(migration_list)

    # to do 
    # add command creation into a text file 

if __name__ == "__main__":
    main()
