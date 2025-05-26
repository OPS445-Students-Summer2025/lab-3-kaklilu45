#!/usr/bin/env python3

#The purpose of this script is to create a Python function that can return the free disk space on a Linux system's root directory

# Author ID: 111658217

import subprocess


def free_space():
    spaceava = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell = True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = spaceava.stdout.decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())
