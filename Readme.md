# ChatBot
First and formost, you will need to have the required programs installed within you system including:
1. Python
2. Django
3. A virtual environment
3. ChatterBot
Next time i will not install chatterBot globally, but insted will install it in the virtual environment

What you need to do is go into the scripts directory and run the `./system.bat` if you are using a windows OS. Note: This application is morely focued on a windows OS. So i have not yet tested this on a Linux System.
So if you are on windows, go to the script directory and simpyly type `system.bat` Now if you see a version number, excellent, otherwise you will need to install the python intepreter. Ensure that the version you install is >3
Once that is done, within the same directory, you are going to run the `python initialise.py` script, this will just check version and check if the required modules are installed. Now if you get an error, then that measn the modules required have not been installed properly. Therefore, install the modules yourself (which is more recommened) or use my script by running `python automatedInstall.py`
Once that is done, you can run the `python initialise.py` again. If you see the version of pipenv, then it has been installed otherwise it has not.


With pipenv, it will install a specific version. So we will have to let user know the version


# Note to self
python 3.12.1