#!/usr/bin/env python

"""my_shell_outline.py:
Simple shell that interacts with the filesystem, e.g., try "PShell>files".

Try to stick to Style Guide for Python Code and Docstring Conventions:
see https://peps.python.org/pep-0008 and https://peps.python.org/pep-0257/

(Note: The breakdown into Input/Action/Output in this script is just a suggestion.)
"""
import shutil
import glob
import os
import pwd
import shutil
import sys
import time
import datetime
import shutil

# ========================
#    files command
#    List file and directory names
#    No command arguments
# ========================
def files_cmd(fields):
    """Return nothing after printing names/types of files/dirs in working directory.
    
    Input: takes a list of text fields
    Action: prints for each file/dir in current working directory their type and name
            (unless list is non-empty in which case an error message is printed)
    Output: returns no return value
    """
    
    if checkArgs(fields, 0):
        for filename in os.listdir('.'):
            if os.path.isdir(os.path.abspath(filename)):
                print("dir:", filename)
            else:
                print("file:", filename)

# ========================
#  info command
#     List file information
#     1 command argument: file name
# ========================
def info_cmd(fields):
    if os.path.exists(fields[1]):
        print("File Name: ", fields[1])
        if os.path.isfile(fields[1]):
            print("Directory/File: file")
        if os.path.isdir(fields[1]):
            info.append("Directory/File: Directory")
        print("Owner: ", os.getlogin())
        print("Last Edited:", datetime.datetime.fromtimestamp(os.path.getmtime(fields[1])))
        print("Size(bytes): ", os.path.getsize(fields[1]))
        if os.access(fields[1], os.X_OK):
            print("Executable: ", False)
        else:
            print("Executable: ", True)
    else:
        print("This file doesn't exist")
# ========================
#  delete command
#     deletes file
#     1 command argument: file name
# ========================

def delete(fields):
    if os.path.exists(fields[1]):         # if the path exists
        if os.path.isfile(fields[1]):     # if it exists
            os.remove(fields[1])          # removes the file
            print("Successfully removed") # tells the user it was a success
        else:
            print("This isn't a file")    # tells the user it isnt a file
    else:
        print("This file doesn't exist")  # tells the user the file doesnt exist

# ========================
#  where command
#     where file
#     0 command arguments
# ========================

def where(fields):
    print("The current directory is: ", os.getcwd())    # gets current directory and tells the user

# ========================
#  up command
#     up file
#     0 command argument
# ========================

def up(fields):
    if os.getcwd() == "/":              
        print("root directory reached" )  # if current directory is / tells the user
    else:
        os.chdir("..")                    # changes to parent directory
        print("You're directory is now: ", os.getcwd()) # tells the user 
# ========================
#  down command
#     down file
#     0 command argument
# ========================

def down(fields):
    if os.path.exists(fields[1]):         # if path exists 
        os.chdir(fields[1])               # changes directory to the one user inputted
        print("You're directory is now: ", os.getcwd())
    else:
        print("Directory doesn't exist")  # tells the user it doesnt exist
# ========================
#  exit command
#     exit file
#     0 command argument
# ========================

def Exit(fields):
    exit()                                # ends the program
# ========================
#  copy command
#     copy file
#     2 command argument
# ========================


def copy(fields):
    if os.path.exists(fields[1]):                        # checks if file exists
        if os.path.isfile(fields[1]):                    # checks if its a file
            if os.path.exists(fields[2]):                # checks if the second one's name exists
                print("This file name is already taken") # prints as seen
            else:
                shutil.copyfile(fields[1],fields[2])     # copy the files and sets the name
        else:
            print("This isn't a file")                   # prints as seen
    else:
         print("This doesn't exist")                     # prints as seen
    

def checkArgs(fields, num):
    """Returns if len(fields)-1 == num and print an error in shell if not.
    
    Input: takes a list of text fields and how many non-command fields are expected
    Action: prints error to shell if the number of fields is unexpected
    Output: returns boolean value to indicate if it was expected number of fields
    """

    numArgs = len(fields) - 1
    if numArgs == num:
        return True
    if numArgs > num:
        print("Unexpected argument", fields[num+1], "for command", fields[0])
    else:
        print("Missing argument for command", fields[0])
        
    return False
# ---------------------------------------------------------------------

def main():
    """Returns exit code 0 (after executing the main part of this script).
    
    Input: no function arguments
    Action: run multiple user-inputted commands
    Output: return zero to indicate regular termination
    """
    
    while True:
        line = input("PShell>")
        fields = line.split()
        # split the command into fields stored in the fields list
        # fields[0] is the command name and anything that follows (if it follows) is an argument to the command
        
        if fields[0] == "files":
            files_cmd(fields)
        elif fields[0] == "info":
            info_cmd(fields)
        elif fields[0] == "delete":
            delete(fields)
        elif fields[0] == "where":
            where(fields)
        elif fields[0] == "up":
            up(fields)
        elif fields[0] == "down":
            down(fields)
        elif fields[0] == "exit":
            Exit(fields)
        elif fields[0] == "copy":
            copy(fields)
        else:
            print("Unknown command", fields[0])
    
    return 0 # currently unreachable code

if __name__ == '__main__':
    sys.exit( main() ) # run main function and then exit
