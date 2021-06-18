import random, string, requests, time
from colorama import Fore
import concurrent.futures
import os
os.system("cls" or "clear")
os.system("title Spectre Username Checker      By SpeedRacer7")
print(Fore.RED+"""

  ██████  ██▓███  ▓█████  ▄████▄  ▄▄▄█████▓ ██▀███  ▓█████ 
▒██    ▒ ▓██░  ██▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀ 
░ ▓██▄   ▓██░ ██▓▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▓██ ░▄█ ▒▒███   
  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄ 
▒██████▒▒▒██▒ ░  ░░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░██▓ ▒██▒░▒████▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░
░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░  ▒       ░      ░▒ ░ ▒░ ░ ░  ░
░  ░  ░  ░░          ░   ░          ░        ░░   ░    ░   
      ░              ░  ░░ ░                  ░        ░  ░
                         ░                                 
                                                                                                  
    Made By : speedracer7
    Github  : Github.com/SpeedRacer07
    Email   : eviniser@gmail.com
    
"""+Fore.WHITE)
time.sleep(.5)
K4 = int(input(Fore.CYAN+"""
        [1] Tiktok Username Checker
        [2] SoundCloud Username Checker
        [3] Github Username Checker
        [4] Twitch Username Checker
        
        [5] Custom Url/Link 
        Select Option [?] : """+Fore.WHITE))
webss = ''
webs = ''
if K4 == 1 :
    webss = 'tiktok.com/@'
    webs = "Tiktok"
elif K4 == 2 :
    webss = 'soundcloud.com/'
    webs = "SoundCloud"
elif K4 == 3 :
    webss = 'github.com/'
    webs = "Github"
elif K4 == 4 :
    webss = 'm.twitch.tv/'
    webs = "Twitch"
elif K4 == 5 :
    webss = str(input("Type Your Costum Link/Url Here (without \'https://\') : "))
    webs = webs
else:
    print('Error Choose Correct Number.. ')
    time.sleep(3)
    quit()

def check(users): 
    try:
        r = requests.get(f'https://{webss}{users}')
        if r.status_code == 200:
            print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {users}'+Fore.WHITE+" <=|"+Fore.CYAN + " [-]")
        else:
            print(Fore.CYAN + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + ' |=>' + Fore.LIGHTMAGENTA_EX + f' {users}'+Fore.WHITE+" <=|" + Fore.CYAN + " [+]")
            f = open("availables.txt", "a", encoding='utf-8')
            f.write(f"{users} | Available or Banned On => {webs} |\n")
    except:
        pass

with open('usernames.txt', 'r') as f:
    users = [line.strip() for line in f]
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check,users)
