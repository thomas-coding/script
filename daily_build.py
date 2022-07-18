#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of daily build

from build import project_build
import socket

def get_host_ip():
    """
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
        return ip

if __name__ == '__main__':

    ip = get_host_ip()
    if ip == '192.168.103.66':
        print('vsi coding server')
        project_build('alexandrite_daily_coding_server')
        project_build('alius_daily_coding_server')
    elif ip == '8.210.111.180':
        print('aliyun server')
    else:
        print('local compute')
        project_build('alexandrite_daily_local')
        project_build('alius_daily_local')
