import random, string, requests, time
from colorama import Fore
import concurrent.futures
import os
os.system("cls" or "clear")
os.system("title Проверка имени пользователя Spectre от SpeedRacer7")
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
                                                                                                  
     Сделано: speedracer7
     Github: Github.com/SpeedRacer07
     Электронная почта: eviniser@gmail.com
    
"""+Fore.WHITE)
time.sleep(.5)
K4 = int(input(Fore.CYAN+"""
         [1] Проверка имени пользователя Tiktok
         [2] Проверка имени пользователя SoundCloud
         [3] Проверка имени пользователя Github
         [4] Проверка имени пользователя Twitch
        
         [5] Пользовательский URL / Ссылка
        Выберите опцию[?] : """+Fore.WHITE))
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
    webss = str(input("Введите здесь свою настраиваемую ссылку / URL(without \'https://\') : "))
    webs = webs
else:
    print('Ошибка Выберите правильный номер .. ')
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
