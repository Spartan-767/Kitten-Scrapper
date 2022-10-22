#!/usr/bin/python
import sys, os
import urllib.request
from urllib.request import urlopen, Request
import time

# Restart ####################
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()
##############################

# OS Check ####################
def OSCheck():
    if os.name == "nt":
      os.system("cls")

    else:
      os.system("clear")
##############################

# Loading Bar ####################
def load_animation():
    # String to be displayed when the application is loading
    load_str = "Starting Kitten Scanner..."
    ls_len = len(load_str)

    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    # used to keep the track of
    # the duration of animation
    counttime = 0

    # pointer for travelling the loading string
    i = 0

    while (counttime != 100):

        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075)

        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str)

        # x->obtaining the ASCII code
        x = ord(load_str_list[i])

        # y->for storing altered ASCII code
        y = 0

        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)

        # for storing the resultant string
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]

        # displaying the resultant string
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()

        # Assigning loading string
        # to the resultant string
        load_str = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1

    # for windows OS
    if os.name == "nt":
        os.system("cls")

    # for linux / Mac OS
    else:
        os.system("clear")

def pog():
    os.system("cls")
    print(" ")
    print("  ___  ___                         ")
    print(" / __|/ __|__ _ _ _  _ _  ___ _ _  ")
    print(" \__ \ (__/ _` | ' \| ' \/ -_) '_| ")
    print(" |___/\___\__,_|_||_|_||_\___|_|   ")
    print("--------------------------------------- ")
    print("     Coded By Spartan by ATech Labs      ")
    print("--------------------------------------- ")
    print("  ===|[ Web Scanner ]|===")
    print("  [01] Scan Web       ")
    print("  [02] Open Scans     ")
    print("  [03] Update         ")
    print("  [00] Exit           ")
    print(" ")
    MenuOp1 = input(" Choose:  ")

    if (MenuOp1 == '01' or MenuOp1 == '1'):
        os.system("cls")
        print("                                          ")
        print(" ===|[ Scan Configuration ]|===           ")
        print("  [01] Scan By Keyword                    ")
        print("  [02] Scan From List                     ")
        print("  [03] Scan From Text File                ")
        print("  [04] Undetected Scan                    ")
        MenuOp2 = input("Option:  ")
        if (MenuOp2 == '01' or MenuOp2 == '1'):
            os.system("cls")
            print(" ")
            keyword = input(" Keyword:  ")
            keywordbyte = keyword.encode()
            link = input(" Link:  ")
            linkbyte = link.encode()
            site = urllib.request.urlopen(linkbyte.decode('ASCII')).read()
            if keywordbyte in site:
                print("Word Detected:")
                print(" ")
                print(keyword)
                time.sleep(20)
            else:
                print(keyword, "not found")
                time.sleep(20)

        if (MenuOp2 == '02' or MenuOp2 == '2'):
            os.system("cls")
            print(" ")
            List1 = input("Input First Word: ")
            keywords = ["List1", "python", "cheese"]
            keywordsbyte = keywords.encode()
            link = input(" Link:  ")
            linkbyte = link.encode()
            site = urllib.request.urlopen(linkbyte.decode('ASCII')).read()
            for keyword in site:
                if keywordbyte in linkbyte:
                    print(keyword)

                else:
                    print(keyword, "not found")

        if (MenuOp2 == '03' or MenuOp2 == '3'):
            os.system("cls")
            print(" Coming Soon ")

        if (MenuOp2 == '04' or MenuOp2 == '4'):
            os.system("cls")
            keyword2 = input(" Keyword:  ")
            url = input(" Link: ")
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            web_byte = urlopen(req).read()
            webpage = web_byte.decode('utf-8')
            if keyword2 in webpage:
                print("Word Detected:")
                print(" ")
                print(keyword2)
                time.sleep(20)
            else:
                print(keyword2, "not found")
                print(url, webpage)
                time.sleep(200)

    elif (MenuOp1 == '02' or MenuOp1 == '2'):
        os.system("cls")
        print("Coming Soon")

    elif (MenuOp1 == '03' or MenuOp1 == '3'):
        os.system("cls")
        print("Not enabled yet")
        os.system("git clone")

    elif (MenuOp1 == '00' or MenuOp1 == '0'):
        os.system("cls")
        print("\n[!] Exiting the Program...")
        sys.exit()

    else:
        os.system("clear")
        print("\n[!] ERROR : Wrong Input")
        time.sleep(1)
        restart_program()

# Driver program
if __name__ == '__main__':
    load_animation()
    os.system("cls")
    print(" ")
    s = input("\n Enter your name: ")
    sys.stdout.write("\n Hello " + str(s) + "\n")
    print("Loading profile")
    time.sleep(4)
    os.system("cls")
    print(" ")
    pog()

