#!/bin/python36

import os

import subprocess as sp

while True:

    print("""

    press 1: Install Docker

    press 2: Load Docker Images

    press 3: Exit
    """)

    print(">>> ",end='')

    ch = int(input())


    if ch == 1:

        os.system("ansible-playbook inst-docker.yml")

        input("press enter to continue")

        os.system("clear")

    elif ch == 2:

        os.system("ansible-playbook load-docker.yml")

        print("\nDocker Images Loaded successfully")

        input("press enter to continue")

        os.system("clear")

    elif ch == 3:

        exit()
















 


