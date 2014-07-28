import constants

__author__ = 'arnav'


def change_path_to_project_url(path):
    path = path.replace('/', '_')
    path = constants.g_proj_basedir + path
    return path


def change_projname_to_dirpath(projname):
    #remove the project's base dir (for eg. the "AOKP/" part
    dirpath = projname.replace(projname[:len(constants.g_proj_basedir)], '')
    dirpath = dirpath.replace('_', '/')
    return dirpath
