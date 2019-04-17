# -*- coding: utf-8 -*-

import os


def before_folder_option(location):
    """location: folder full path"""
    if not os.path.exists(location):
        os.makedirs(location)
    return True


def after_folder_option(location):
    """location: folder full path"""
    return True


def retire_folder(location, new_name):
    """
    location: folder full path
    new_name: new folder name (not path, just a name string)
    """
    parent_folder = os.path.dirname(location)
    os.rename(location, os.path.join(parent_folder, new_name))
    return True
