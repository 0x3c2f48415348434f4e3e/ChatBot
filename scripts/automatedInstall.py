import sys
import subprocess
'''
def checkChatterBot() -> int:
    if('ChatterBot' in sys.modules):
        return 0
    #installation
    subprocess.run("pip install chatterbot",stdout=True)
A virtual environment will be created where we will install chatterbot
    '''
def checkVirtualEnv() -> int:
    if('pipenv' in sys.modules):
        return 0
    #installation
    subprocess.run("pip install --user pipenv",stdout=True)
#checkChatterBot()
checkVirtualEnv()

