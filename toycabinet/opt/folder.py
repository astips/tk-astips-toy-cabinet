# -*- coding: utf-8 -*-

import os


def before_toy_folder_option(toy_location):
    if not os.path.exists(toy_location):
        os.makedirs(toy_location)
    return True


def after_toy_folder_option(toy_location):
    pass
