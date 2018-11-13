
print(" \t    |  _____     __             __ __               __                    |")
print(" \t    | / ___/_ __/ /  ___ ____  / // /__ _____    __/ /__ ___              |")
print("\t    | / /__/ // / _ \/ -_) __/ / _  / _ `(_-< |/|/ /  '_/(_-<             |")
print("\t    | \___/\_, /_.__/\__/_/   /_//_/\_,_/___/__,__/_/\_\/___/             |")
print("\t    |   /___/                                               Anonymous     |")
print("\t    |               Team: | Hawk Hacktivist | Hunk |                      | ")





import time

import sys

sam = input("Enter Email For Hacking  : ")

pppp = input("Enter the name of your text file - please use / backslash when typing in directory path: ");  #User will enter the name of text file for me

f = open(pppp,"r+")




file_name = pppp


with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
        time.sleep(3)