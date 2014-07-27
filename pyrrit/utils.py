import constants

__author__ = 'arnav'

def change_path_to_project_url(path):
    path = path.replace('/', '_')
    return path