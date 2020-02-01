The goal of this code is to quickly create an ansible playbook from which one or multiple machines can be set up.
It is rather difficult to create an automated pc setup script for windows because of the lack of terminal commands to install software.
Using chocolatey (https://chocolatey.org) however a solid base installation can be automated. This python script aims to do just that.

1. Install the Software of choice through chocolatey.
2. Run main.py to generate ansible code on the machine on which you installed the chocolatey software.

The generatedAnsibleCode.yml was created in the same directory as the python program.
You can use this playbook to reinstall windows on other machines.