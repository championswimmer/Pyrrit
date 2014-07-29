#!/usr/bin/python3
import sys

import listchanges
import pullchange


__author__ = 'arnav'


def print_help():
    print("Usage : pyrrit [mode [parameters]]")
    print("Where mode can be \n")
    print("list [dirpath]          - Show all open patches [for given directory path]")
    print("upload")
    print("pull ps#                - Pull the given patchset(s)")
    print("pstest ps# device       - Pull the given patchset(s), and make a build for device to test")
    print("\n")
    print("Some example commands\n")
    print("pyrrit list device/sony/common")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_help()

    elif sys.argv[1] == "help":
        print_help()

    elif sys.argv[1] == "pull":
        if len(sys.argv) == 3:
            pullchange.pull_one_change(sys.argv[2])
        else:
            print('Please mention the change # of patch you want to pull')

    elif sys.argv[1] == "list":
        if len(sys.argv) == 3:
            listchanges.show_proj_list(sys.argv[2])
        else:
            listchanges.show_all_list()

    elif sys.argv[1] == "upload":
        print("upload")
        ##TODO: write upload funciton

    else:
        print("Bad argument passed")
        print_help()

