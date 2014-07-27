#!/usr/bin/python3
import sys

__author__ = 'arnav'

try :
    if sys.argv[1] == "pull":
        print("pull")
        ##TODO: write pull funciton

    if sys.argv[1] == "list":
        print("upload")
        ##TODO: write list funciton

    if sys.argv[1] == "upload":
        print("upload")
        ##TODO: write upload funciton
except:
    print("Usage : pyrrit [mode [parameters]]")
    print("Where mode can be \n")
    print("list [project]          - Show all recent patches on this project")
    print("upload")
    print("pull [ps#]              - Pull the given patchset")
    print("pstest [ps#] [device]   - Pull the given patchsets, and make a build for device to test")