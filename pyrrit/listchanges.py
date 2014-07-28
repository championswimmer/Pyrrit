import json

import requests

import constants
import utils


__author__ = 'arnav'

l_url = "http://" + constants.g_url + "/changes/?q=status:open"

col_y = '\033[93m'
col_p = '\033[95m'
col_g = '\033[92m'
col_0 = '\033[0m'


def show_list(url):
    resp_str = requests.get(url).text

    # ugly hack because gerrit's json has 4 stupid characters in the first line
    resp_str = resp_str.replace(resp_str[:4], '')

    json_data = json.loads(resp_str)
    for item in json_data:
        print(col_y + str(item.get('_number')) + col_0 + "\t" + item.get('subject'))
        print("  " + col_g + item.get('project') + col_0 + "\n")


def show_all_list():
    show_list(l_url)


def show_proj_list(proj_path):
    proj_url_path = utils.change_path_to_project_url(proj_path)
    full_url = l_url + "+project:" + proj_url_path
    show_list(full_url)


if __name__ == '__main__':
    show_all_list()