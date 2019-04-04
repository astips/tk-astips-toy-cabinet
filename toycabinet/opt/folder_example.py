# -*- coding: utf-8 -*-

import os
from my_office import rpc  # my_office is a fake module ~ ~


def before_toy_folder_option(toy_location):
    if not os.path.exists(toy_location):
        rpc.create_folder(toy_location)  # 如果不存在，通过RPC创建文件夹
    rpc.chmod(toy_location, '777', recursive=True)   # 通过RPC更改文件夹权限
    return True


def after_toy_folder_option(toy_location):
    rpc.chown(toy_location, 'ple:ple', recursive=True)  # 通过RPC更改文件夹所有人
    rpc.chmod(toy_location, '755', recursive=True)  # 通过RPC更改文件夹权限
    return True
