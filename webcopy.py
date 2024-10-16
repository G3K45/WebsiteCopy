import requests
import fade 
from fade import *
import platform
import os

def exit1():
    option = input("Do you want to exit the program? [y]yes [n]no:")
    if option == "y":
        banner2()
    elif option == "n":
        main()
    else:
        clearscreen()
        exit1()

def clearscreen():
    sys = platform.system
    if sys == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def banner2():
    banner = """
      ________ ________   ________  ________ _______________.___.___________ 
      /  _____/ \_____  \  \_____  \ \______ \\______   \__  |   |\_   _____/ 
     /   \  ___  /   |   \  /   |   \ |    |  \|    |  _//   |   | |    __)_  
     \    \_\  \/    |    \/    |    \|    `   \    |   \\____   | |        \ 
      \______  /\_______  /\_______  /_______  /______  // ______|/_______  / 
             \/         \/         \/        \/       \/ \/               \/  
    |------------------------------------------------------------------------|
    |                        CODED BY: G3K45                                 |
    |------------------------------------------------------------------------|
    """
    print(fade.fire(banner))

def banner():
    banner = """
     __      _______________________  _________.__  __         _________  ________ _______________.___.
    /  \    /  \_   _____/\______   \/   _____/|__|/  |_  ____ \_   ___ \ \_____  \\______   \__  |   |
    \   \/\/   /|    __)_  |    |  _/\_____  \ |  \   __\/ __ \/    \  \/  /   |   \|     ___//   |   |
     \        / |        \ |    |   \/        \|  ||  | \  ___/\     \____/    |    \    |    \____   |
      \__/\  / /_______  / |______  /_______  /|__||__|  \___  >\______  /\_______  /____|    / ______|
           \/          \/         \/        \/               \/        \/         \/          \/       
    """
    print(fade.blackwhite(banner))

def main():
    clearscreen()
    banner()
    url = input("Enter URL:")
    path = input("Enter Directory or Filename:")
    request = requests.get(url)
    response = request.text
    fopen = open(path+".html", "w")
    fopen.write(response)
    exit1()

main()