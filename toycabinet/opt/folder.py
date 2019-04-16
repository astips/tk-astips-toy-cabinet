# -*- coding: utf-8 -*-

import os


def before_folder_option(location):
    if not os.path.exists(location):
        os.makedirs(location)
    return True


def after_folder_option(location):
    return True


def retire_folder(location, new_name):
    parent_folder = os.path.dirname(location)
    os.rename(location, os.path.join(parent_folder, new_name))
    return True
