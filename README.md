# pyrrit
#### pyrrit is the missing link between an android source tree and it's gerrit review

## Introduction

<b>pyrrit</b> was written by me to help myself and my codevelopers
at [AOKP](http://aokp.co)    
Our source code is [here](http://github.com/AOKP)   
and our code review [here](http://gerrit.aokp.co)   

The idea of pyrrit is to be able to view open changes on the code review,   
pull them, test them, verify/review them etc right from the command line  
without having to open gerrit in a browser.

## Installation

In it's current form <b>pyrrit</b> is suitable to be used only for an  
AOSP-like source code tree, although it can be adapted for other needs.

The <i>pyrrit</i> folder (containing \__main\__.py, utils.py etc) should  
go into the build folder. i.e. $source_top/build/tools/pyrrit

You will need to edit the contents of build/pyrrit/config.py according to  
your environment. Your gerrit's location and ports will be different ;)
For eg. at AOKP, a project like <i>AOKP/vendor_aokp</i> maps to a project  
directory at <i>$source_top/vendor/aokp</i>

## Usage

You can make calls to pyrrit like 
    
    python2.7 build/tools/pyrrit  [arguments]

Or, preferrably, you can add a function to your <i>envsetup.sh</i>

    function pyrrit()
    {
        T=$(gettop)
        python2.7 ${T}/build/tools/pyrrit $@
    }

Then using pyrrit becomes easier like

    . build/envsetup.sh
    pyrrit [arguments]

Running pyrrit without arguments or running "pyrrit help" will show  
you the help text. For other functions continue reading.

### Listing Changes
pyrrit can list all open changes on gerrit using this command

    pyrrit list

Or you can check your open changes of singular projects like

    pyrrit list vendor/aokp
    
Note, you dont need to provide the project name like "AOKP/vendor_aokp"  
Just provide the directory path, and pyrrit will figure the rest.

### Pulling Changes
pyrrit can pull changes using a command like this

    pyrrit pull 17723

This will get change no. 17723, and cherry-pick it to it's project directory.
You can call this function from anywhere. Pyrrit will always cherry-pick into  
the correct location only. It wont pull stuff into wrong projects. :)

You can pull multiple changes together

    pyrrit pull 17723 17712 17775
Generally pyrrit pulls the most current revision of the given change. But if  
you wish to, you can specify the change revision no.

    pyrrit pull 17723 17712/2 17775/1
Also if you leave the revision empty like this

    pyrrit pull 17723/
In that case pyrrit will ask you for revision number when pulling that change

### Pulling a topic
pyrrit can pull all changes of a particular topic using a command like this

    pyrrit topicpull topic_name
This pulls all changes (in all projects and directories) that have "topic_name" as their topic. 