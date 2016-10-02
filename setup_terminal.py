from requests import get
from os import system

print("disabling stuff")
system('echo "stty -ixon" >> .bashrc')
print("setting up vimrc")
system("cp vimrc ~/.vimrc")
print("setting up ycm_conf file for YouCompleteMe autocompleter")
system("cp ycm_extra_conf.py ~/.vim/.ycm_extra_conf.py")
print("Installing all plugins please wait ...")
system("vim +PluginInstall +qall")

print("setup complete enjoy")
