import sys
import subprocess

'''
System requirments

For the installation of this, we will be using several libraries such as ChatterBot,
a veritual enviroment(This is where we will install django) and more if needed

'''


'''check our python environment (Must be greater than version 3)
We can make use of the sys module
'''

print("Script initialising")

'''
Some error occured, so a virtual environment wil be created and we will install chatterbot in there
def checkChatterBot() -> int:
    if('ChatterBot' in sys.modules):
        return 1
    return 0
'''

def checkVirtualEnv() -> int:
    if('pipenv' in sys.modules):
        return 1
    return 0

py_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)
#The python version we need is 3.6 or greather
if(int(py_version[0]) >= 3 and int(py_version[2:]) >= 6):
    #sys.exit(0)
    print("Python version installed is suitable\n")
    '''
    if(checkChatterBot):
        raise Exception(
            'The module ChatterBot can not be indentified. Please Install the latest verion of ChatterBot. (Note: I have included a script to do this, but to be more safer do it your self)'
        )
    '''
    '''
    if(checkVirtualEnv):
        raise Exception(
            'The module pipenv can not be indentified. Please Install the latest verion of pipenv. (Note: I have included a script to do this, but to be more safer do it your self)'
        )
    else:
        print("ChatterBot version andpipenv version are suitable\n")
    '''
    subprocess.run("pipenv --version",stdout=True)
    sys.exit(0)

raise Exception(
    'You are trying to use Python (major version) {0} which is not recommended. insted install {1}'.format(py_version,"3.6")
)
