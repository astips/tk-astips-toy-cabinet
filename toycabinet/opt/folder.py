# -*- coding: utf-8 -*-

import os


def before_toy_folder_option(toy_location):
    if not os.path.exists(toy_location):
        os.makedirs(toy_location)
    return True


def after_toy_folder_option(toy_location):
    return True


def retire_toy_folder(toy_location, toy_item):
    # shutil.rmtree(location)  # We will not delete it, just rename & tag it as retired.
    root_path = os.path.dirname(toy_location)
    os.rename(
        toy_location, os.path.join(root_path, '{0}___RETIRED___ID_{1}'.format(toy_item.path, toy_item.id))
    )
    return True
