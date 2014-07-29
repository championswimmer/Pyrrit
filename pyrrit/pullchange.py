import json
import os
import sys
from pyatspi import value
import config
import utils

__author__ = 'arnav'

p_url = "http://" + config.g_url + "/changes/"
top_dir = os.environ['T']


def cherry_pick_change(proj_name, url, ref):
    dir_path = utils.change_projname_to_dirpath(proj_name)
    cd_command = "cd " + top_dir + "/" + dir_path

    fetch_command = "git fetch " + url + " " + ref
    cherrypick_command = "git cherry-pick FETCH_HEAD"


    os.system(cd_command + " && " + fetch_command + " && " + cherrypick_command)


def pull_one_change(change_no):
    url = p_url + change_no + "?o=ALL_REVISIONS"
    json_data = utils.get_json_from_url(url)
    proj_name = json_data.get('project')
    rev_numbers = []
    rev_branches = []
    rev_urls = []
    revisions = json_data.get("revisions")
    for revision in revisions:
        rev_numbers.append(json_data["revisions"][revision].get("_number"))
        rev_branches.append(json_data["revisions"][revision]['fetch']['anonymous http']['ref'])
        rev_urls.append(json_data["revisions"][revision]['fetch']['anonymous http']['url'])
    rev = len(rev_numbers) - 1
    cherry_pick_change(proj_name, rev_urls[rev], rev_branches[rev])
