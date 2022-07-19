#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of project

import subprocess
import os
import time

current_dir = os.path.split(os.path.realpath(__file__))[0]

class Project:
    '''
    Class for dealing with code project.
    '''
    compile_time = 0
    code_path = current_dir
    default_release_path = current_dir + "/daily_build"

    def __init__(self, name, dir=current_dir):
        self.name = name
        self.code_path = dir

    def compile(self, module = '', prebuild = ''):
        start_time = time.time()
        if prebuild != '':
            cmd = 'cd %s/build && ./build.sh %s' %(self.code_path, prebuild)
            subprocess.run(cmd, shell=True)
        cmd = 'cd %s/build && ./build.sh %s %s' %(self.code_path, self.name, module)
        print(cmd)
        subprocess.run(cmd, shell=True)
        end_time = time.time()
        self.compile_time = end_time- start_time
        return 0

    def cleanup(self, repo_cmd = ''):
        # new or clean
        if (os.path.exists(self.code_path) == False):
            print('%s not exit, create' %(self.code_path))
            cmd = 'mkdir -p %s'  %(self.code_path)
            subprocess.run(cmd, shell=True)
            cmd = 'cd %s/ && %s'  %(self.code_path, repo_cmd)
            print(cmd)
            subprocess.run(cmd, shell=True)
        else:
            cmd = 'cd %s/ && repo forall -c "git reset --hard; git clean -dxf"'  %(self.code_path)
            subprocess.run(cmd, shell=True)
            cmd = 'cd %s/ && rm -rf out'  %(self.code_path)
            subprocess.run(cmd, shell=True)
        return 0

    def reposync(self):
        cmd = 'cd %s/ && repo sync'  %(self.code_path)
        subprocess.run(cmd, shell=True)
        return 0

    def notify(self, email):
        if email != '':
            cmd = 'echo Succeed used %d s | s-nail  -s "%s Build Succeed" %s' %(self.compile_time, self.name, email)
            subprocess.run(cmd, shell=True)
        return 0

    def release(self, release_path = default_release_path):
        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

        # Make release dir
        release_dir = release_path + "/" + date
        if (os.path.exists(release_dir) == True):
            cmd = 'rm -rf %s'  %(release_dir)
            subprocess.run(cmd, shell=True)
        cmd = 'mkdir -p %s'  %(release_dir)
        subprocess.run(cmd, shell=True)

        # Gather build log
        #cmd = 'cd %s/ && mv build.log %s'  %(self.code_path, release_dir)
        #subprocess.run(cmd, shell=True)

        # Gather snapshot
        cmd = 'cd %s/ && repo manifest -r -o %s.xml'  %(self.code_path, date)
        subprocess.run(cmd, shell=True)
        cmd = 'cd %s/ && mv %s.xml %s'  %(self.code_path, date, release_dir)
        subprocess.run(cmd, shell=True)

        # Gather changes
        change_file = date + "_changes.txt"
        cmd = "cd %s/ && repo forall -c git log --since='24 hours ago' > %s"  %(self.code_path, change_file)
        subprocess.run(cmd, shell=True)
        cmd = 'cd %s/ && mv %s %s'  %(self.code_path, change_file, release_dir)
        subprocess.run(cmd, shell=True)

        # Gather image
        images_dir = "out/" + self.name + "/images"
        cmd = 'cd %s/ && tar -zcf %s.tar.gz %s'  %(self.code_path, date, images_dir)
        subprocess.run(cmd, shell=True)
        cmd = 'cd %s/ && mv %s.tar.gz %s'  %(self.code_path, date, release_dir)
        subprocess.run(cmd, shell=True)

        return 0
