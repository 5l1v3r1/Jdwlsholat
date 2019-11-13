#!/usr/bin/python
# Prayer Schedule
# Coded by Senja
# Github: github.com/thesixtynine/Prayer

import os, sys, time, requests, json


def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

logo = """\033[1;77m
        ______   ______     ______     __  __
       /\  == \ /\  == \   /\  __ \   /\ \_\ \   
       \ \  _-/ \ \  __<   \ \  __ \  \ \____ \  
        \ \_\    \ \_\ \_\  \ \_\ \_\  \/\_____\ 
         \/_/     \/_/ /_/   \/_/\/_/   \/_____/ 
"""

def main():
    os.system('clear')
    os.system("reset")
    time.sleep(1)
    print
    print logo
    print
    print "\033[0m[\033[1;94m#\033[0m] Prayer Schedule"
    print "\033[0m[\033[1;93m*\033[0m] Coded by Senja"
    print "\033[0m[\033[1;96m&\033[0m] My Github: @thesixtynine"
    time.sleep(1)
    print
    srch = raw_input("\033[0m[\033[1;95m+\033[0m] \033[1;77mCity: \033[0m")
    print
    write ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mChecking ...')
    time.sleep(3)
    print ""
    try:
        r = requests.get("https://time.siswadi.com/pray/"+srch)
        q = json.loads(r.text)
        subuh = q["data"]["Fajr"]
        dzuhur = q["data"]["Dhuhr"]
        ashar = q["data"]["Asr"]
        magrib = q["data"]["Maghrib"]
        isha = q["data"]["Isha"]
        date = q["time"]["date"]
        waktu = q["time"]["time"]
        lokasi = q["location"]["address"]
        print
        print "\033[0m[\033[1;92m^\033[0m] \033[1;77mSubuh   : \033[0m"+subuh
        print "\033[0m[\033[1;92m^\033[0m] \033[1;77mDzuhur  : \033[0m"+dzuhur
        print "\033[0m[\033[1;92m^\033[0m] \033[1;77mAshar   : \033[0m"+ashar
        print "\033[0m[\033[1;92m^\033[0m] \033[1;77mMaghrib : \033[0m"+magrib
        print "\033[0m[\033[1;92m^\033[0m] \033[1;77mIsya    : \033[0m"+isha
        print "\033[0m[\033[1;94m$\033[0m] \033[1;77mDate    : \033[0m"+date
        print "\033[0m[\033[1;93m@\033[0m] \033[1;77mTime    : \033[0m"+waktu
        print
        print "\033[0m[\033[1;95m#\033[0m] \033[1;77mStatus  : \033[0m"+q["status"]
        print
        exit(1)
    except KeyError:
        print "\033[0m[\033[1;91m!\033[0m] \033[1;77mNot found"
        print
        exit(1)

if __name__=="__main__":
    main()
