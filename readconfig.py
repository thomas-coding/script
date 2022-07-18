#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of server

import os
import configparser

current_dir = os.path.abspath('.')
configpath = os.path.join(current_dir, "config.ini")

class ReadConfig:
    '''
    Class for read config
    '''
    project_name = ''
    code_path = ''
    release_path = ''
    notify_email = ''
    repo_cmd = ''
    prebuild = ''

    def __init__(self, section):
        cf = configparser.ConfigParser()
        cf.read(configpath)
        self.project_name = cf.get(section, "project_name")
        self.code_path = cf.get(section, "code_path")
        self.release_path = cf.get(section, "release_path")
        self.notify_email = cf.get(section, "notify_email")
        self.repo_cmd = cf.get(section, "repo_cmd")
        self.prebuild = cf.get(section, "prebuild")

    def get_project_name(self):
        return self.project_name

    def get_code_path(self):
        return self.code_path

    def get_release_path(self):
        return self.release_path

    def get_notify_email(self):
        return self.notify_email

    def get_repo_cmd(self):
        return self.repo_cmd

    def get_prebuild(self):
        return self.prebuild
