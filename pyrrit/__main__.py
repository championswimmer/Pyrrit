#!/usr/bin/python3
import sys
import utils

__author__ = 'arnav'


# try :
if sys.argv[1] == "pull":
    print("pull")
    ##TODO: write pull funciton

if sys.argv[1] == "list":
    import listchanges
    print("Listing changes from " + listchanges.url)
    listchanges.show_all_list()

if sys.argv[1] == "upload":
    print("upload")
    ##TODO: write upload funciton
# except:
#     print("Usage : pyrrit [mode [parameters]]")
#     print("Where mode can be \n")
#     print("list [project]          - Show all recent patches on this project")
#     print("upload")
#     print("pull [ps#]              - Pull the given patchset(s)")
#     print("pstest [ps#] [device]   - Pull the given patchset(s), and make a build for device to test")