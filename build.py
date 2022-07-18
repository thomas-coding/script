#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

from readconfig import ReadConfig
from project import Project

class Build:
    '''
    Class for build
    '''

    project_name = ''
    code_path = ''
    release_path = ''
    notify_email = ''
    repo_cmd = ''
    prebuild = ''

    def __init__(self, config_section):

        self.server = ReadConfig(config_section)
        self.project_name = self.server.get_project_name()
        self.code_path = self.server.get_code_path()
        self.release_path = self.server.get_release_path()
        self.notify_email = self.server.get_notify_email()
        self.repo_cmd = self.server.get_repo_cmd()
        self.prebuild = self.server.get_prebuild()

        self.project = Project(self.project_name, self.code_path)

    def build(self):
        self.project.cleanup(self.repo_cmd)
        self.project.reposync()
        self.project.compile('', self.prebuild)
        self.project.release(self.release_path)
        self.project.notify(self.notify_email)
        return 0

def project_build(config_section):
    build = Build(config_section)
    build.build()
    return 0
