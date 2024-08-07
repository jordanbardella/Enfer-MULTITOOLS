import os
import pystyle 
import time
import webview as w
from colorama import init, Fore, Style
import argparse
import requests
import subprocess

os.system('mode con: cols=128 lines=25')
pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE

def freerdp():
    subprocess.run(["python", "tools/FreeRDP.py"])

def censys():
    subprocess.run(["python", "tools/CensysCLI.py"])

def doxtracker():
    subprocess.run(["python", "tools/DoxTracker.py"])

def phonetools():
    subprocess.run(["python", "tools/PhoneLookup.py"])

def usernamechecker():
    subprocess.run(["python", "tools/UsernameChecker.py"])
    
def cvescan():
    subprocess.run(["python", "tools/cvescan.py"])
    
def vulnscan():
    subprocess.run(["python", "tools/WebVulnScan.py"])
    
def hash():
    subprocess.run(["python", "tools/hash.py"])
    
def dehash():
    subprocess.run(["python", "tools/dehash.py"])
    
def searchfivem():
    subprocess.run(["python", "tools/fivemsearch.py"])
    
def scrapeof():
    subprocess.run(["python", "tools/scrapeof.py"])
    
def githubemail():
    subprocess.run(["python", "tools/githubemail.py"])
    
def sqliscan():
    subprocess.run(["python", "tools/sqliscan.py"])
    
logo = r + f'''
           ███████╗███╗   ██╗███████╗███████╗██████╗ 
           ██╔════╝████╗  ██║██╔════╝██╔════╝██╔══██╗│Version : 1.0
           █████╗  ██╔██╗ ██║█████╗  █████╗  ██████╔╝├─────────────
           ██╔══╝  ██║╚██╗██║██╔══╝  ██╔══╝  ██╔══██╗│{pc_username}\'s PC
           ███████╗██║ ╚████║██║     ███████╗██║  ██║├─────────────
           ╚══════╝╚═╝  ╚═══╝╚═╝     ╚══════╝╚═╝  ╚═╝│.gg/enfer

'''
ascii = pystyle.Center.XCenter(logo)
def menu():
    options = f''' 
    ╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                                 ═══╗
    ║   ({b}01{r}) > RemoteDesktop             ║ ║   ({b}10{r}) > SearchScrapeFivem          ║ ║   ({b}19{r}) > N/A                          ║
        ({b}02{r}) > CensysCLI                       ({b}11{r}) > ScrapeOF                         ({b}20{r}) > N/A
        ({b}03{r}) > DoxTracker                      ({b}12{r}) > GithubGetEmail                   ({b}21{r}) > N/A
        ({b}04{r}) > PhoneLookup                     ({b}13{r}) > SqliScan                         ({b}22{r}) > N/A
        ({b}05{r}) > UsernameChecker                 ({b}14{r}) > N/A                              ({b}23{r}) > N/A
        ({b}06{r}) > CVEScanner                      ({b}15{r}) > N/A                              ({b}24{r}) > N/A
        ({b}07{r}) > WebVulnScanner                  ({b}16{r}) > N/A                              ({b}25{r}) > N/A
        ({b}08{r}) > Hash                            ({b}17{r}) > N/A                              ({b}26{r}) > N/A
    ║   ({b}09{r}) > UnHash                    ║ ║   ({b}18{r}) > N/A                         ║ ║  ({b}27{r}) > N/A                          ║
    ╚═══                              ═══╝ ╚═══                                ═══╝ ╚═══                                ═══╝
'''
    os.system('cls' if os.name == 'nt' else 'clear')
    ops = pystyle.Center.XCenter(options)
    print(ascii)
    print(ops)
    
def update_title(title):
    os.system(f"title ENFER - {pc_username}'s PC ({title})")
    
os.system(f"title ENFER - {pc_username}\'s PC (MENU)")
menu()
print(f'┌──<{pc_username}@ENFER>─[~]')
i = input(f'└──╼ $ {b}').lstrip("0")
choice = i.upper()
try:
   
    options = {
        '1': ('RemoteDesktop', freerdp),
        '2': ('CensysCLI', censys),
        '3': ('DoxTracker', doxtracker),
        '4': ('PhoneLookup', phonetools),
        '5': ('UsernameChecker', usernamechecker),
        '6': ('CVEScanner', cvescan),
        '7': ('WebVulnScanner', vulnscan),
        '8': ('Hash', hash),
        '9': ('UnHash', dehash),
        '10': ('SearchScrapeFivem', searchfivem),
        '11': ('ScrapeOF', scrapeof),
        '12': ('GithubGetEmail', githubemail),
        '13': ('SqliScanner', sqliscan),
    }

    title, cf = options.get(choice, (None, None))
    
    if cf:
        os.system('cls' if os.name == 'nt' else 'clear')
        update_title(title)
        print(ascii)
        cf()
        time.sleep(1)
    else:
        menu()
except Exception as e:
    print(Fore.RED + f"[!]Error: {e}")