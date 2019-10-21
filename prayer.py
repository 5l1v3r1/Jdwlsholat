#!/usr/bin/python
# Life Of Programmer
# Coded By The Sixty Nine

#module
import os,sys,time
import requests,json

coded = "thesixtynine"

#Warna

merah  = "\033[1;31m"
lime   = "\033[1;32m"
kuning = "\033[1;33m"
biru   = "\033[1;34m"
ungu   = "\033[1;35m"
blue   = "\033[1;36m"
putih  = "\033[1;47m"
tutup  = "\033[0m"

def main():
    os.system('clear')
    os.system("reset")
    time.sleep(1)
    print ""
    os.system("toilet -f script -F gay Sholat")
    print ""
    print "        [=\033[0m\033[104m Prayer Schedule \033[0m=] \033[1;33mv0.3"
    print ""
    print tutup+"["+blue+"#"+tutup+"] \033[0m\033[1;77mCoded by     : \033[1;36mThe Sixty Nine\033[0m ]"
    print tutup+"["+lime+"#"+tutup+"] \033[0m\033[1;77mSource       : \033[1;32mhttps://github.com/thesixtynine\033[0m ]"
    print ""
    cari = raw_input("["+biru+"+"+tutup+"] \033[0m\033[1;77mCity : "+biru)
    print tutup+"\033[0m[\033[93;1m*\033[0m] \033[1;77mPlease wait ...\033[0m"
    time.sleep(2)
    print ""
    try:
        r = requests.get("https://time.siswadi.com/pray/"+cari)
        q = json.loads(r.text)
        subuh = q["data"]["Fajr"]
        dzuhur = q["data"]["Dhuhr"]
        ashar = q["data"]["Asr"]
        magrib = q["data"]["Maghrib"]
        isha = q["data"]["Isha"]
        date = q["time"]["date"]
        waktu = q["time"]["time"]
        lokasi = q["location"]["address"]
        print tutup+"["+ungu+">"+tutup+"] Subuh   : "+ungu+subuh
        print tutup+"["+ungu+">"+tutup+"] Dzuhur  : "+ungu+dzuhur
        print tutup+"["+ungu+">"+tutup+"] Ashar   : "+ungu+ashar
        print tutup+"["+ungu+">"+tutup+"] Maghrib : "+ungu+magrib
        print tutup+"["+ungu+">"+tutup+"] Isya    : "+ungu+isha
        print tutup+"["+kuning+"*"+tutup+"] Date    : "+kuning+date
        print tutup+"["+blue+"*"+tutup+"] Time    : "+blue+waktu
        print tutup+"["+merah+"*"+tutup+"] Address : "+merah+lokasi
        print tutup+"["+biru+"*"+tutup+"] Status  : "+biru+q["status"]
        print tutup+""
        print tutup+""
    except KeyError:
        print tutup+"["+merah+"!"+tutup+"] Not found."
        print tutup+""
        print tutup+""
        exit()

if __name__=="__main__":
    main()
