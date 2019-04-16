# -*- coding: utf-8 -*-

import os
from my_office import rpc  # my_office is a fake module ~ ~


def before_folder_option(location):
    if not os.path.exists(location):
        rpc.create_folder(location)  # 如果不存在，通过RPC创建文件夹
    rpc.chmod(location, '777', recursive=True)   # 通过RPC更改文件夹权限
    return True


def after_folder_option(location):
    rpc.chown(location, 'ple:ple', recursive=True)  # 通过RPC更改文件夹所有人
    rpc.chmod(location, '755', recursive=True)  # 通过RPC更改文件夹权限
    return True


def retire_folder(location, new_name):
    parent_folder = os.path.dirname(location)
    rpc.rename_folder(location, os.path.join(parent_folder, new_name))
    return True
