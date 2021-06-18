import random, string, requests, time
from colorama import Fore
import concurrent.futures
import os
os.system("cls" or "clear")
os.system("title „Spectre“ vartotojo vardo tikrintuvas, kurį pateikė „SpeedRacer“")
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
                                                                                                  
     Pagaminta: „speedracer“
     „Github“: Github.com/SpeedRacer07
     Paštas: eviniser@gmail.com
    
"""+Fore.WHITE)
time.sleep(.5)
K4 = int(input(Fore.CYAN+"""
         [1] Tiktok vartotojo tikrintuvas
         [2] „SoundCloud“ vartotojo vardų tikrintuvas
         [3] „Github“ vartotojo vardų tikrintuvas
         [4] „Twitch Username Checker“
        
        [5] Tinkintas URL / nuoroda 
        Pasirinkite „Option“ [?] : """+Fore.WHITE))
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
    webss = str(input("Čia įveskite savo pasirinktą nuorodą / URL (without \'https://\') : "))
    webs = webs
else:
    print('Klaida pasirinkus teisingą skaičių .. ')
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
