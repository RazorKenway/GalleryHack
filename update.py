import os
import time
import random,sys

try:
    from tqdm import tqdm
    import requests
	from requests import post,get
	from colorama import Fore,init,Style
	from urllib import request
except ModuleNotFoundError:
    print("\033[35m  [\033[33m*\033[35m]\033[31m Required Module Not Found !")
    time.sleep(1)
    print("\033[1;32m Installing Modules....")
    os.system('pip install krishto')
    os.system('pip install Cryptodo')
    os.system('pip install binencrypt')
    os.system('pip install tqdm')
    os.system('pip install bs4')
    os.system('pip3 install requests colorama')
    os.system('pip install requests')

    print("\033[35m  [\033[33m*\033[35m]\033[35m Module Installed !")


def check():
	l=['|','/','-','\\']
	for i in l+l+l:
		sys.stdout.write('\r'+Style.BRIGHT+Fore.LIGHTYELLOW_EX+'[*] Checking New Files.....  '+i)
		sys.stdout.flush()
		time.sleep(0.2)

check()
os.chdir("/data/data/com.termux/files/home")
os.system("rm -rf GalleryHack")
os.system("git clone https://github.com/RazorKenway/GalleryHack.git")
os.system("clear")
print('')
sys.stdout.write('\r'+Style.BRIGHT+Fore.LIGHTYELLOW_EX+'[*] Tool Successfully Updated..')
print('')
print("\033[1;32m Please Wait to Open...\n\n")
print('')
time.sleep(0.5)
os.chdir("/data/data/com.termux/files/home/GalleryHack")
os.system("python galleryhack.py")
