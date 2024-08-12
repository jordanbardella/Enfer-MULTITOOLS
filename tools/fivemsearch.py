import re
from colorama import init, Fore, Style
import pystyle 
import os
import subprocess
import time
import py7zr

def menu():
    subprocess.run(["python", "main.py"])

y = Fore.YELLOW
r = Fore.RED
b = Fore.BLUE
pc_username = os.getlogin()

def sf(fp, s):
    with open(fp, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    results = {}
    for line in lines:
        if s in line:
            nm = re.search(r"Name: (\w+)", line)
            im = re.search(r"Identifiers: (\[.*?\])", line)
            em = re.search(r"Endpoint: (\S+)", line)
            
            if nm and im and em:
                name = nm.group(1)
                identifiers = im.group(1)
                endpoint = em.group(1)

                identifiers = eval(identifiers)
                discord = None
                live = None
                xbl = None
                fivem = None
                license1 = None
                license2 = None

                for identifier in identifiers:
                    if identifier.startswith("discord:"):
                        discord = identifier.split(":")[1]
                    elif identifier.startswith("live:"):
                        live = identifier.split(":")[1]
                    elif identifier.startswith("xbl:"):
                        xbl = identifier.split(":")[1]
                    elif identifier.startswith("fivem:"):
                        fivem = identifier.split(":")[1]
                    elif identifier.startswith("license:"):
                        if not license1:
                            license1 = identifier.split(":")[1]
                        else:
                            license2 = identifier.split(":")[1]

                key = (name, discord, license1)
                if key not in results:
                    results[key] = {
                        "name": name,
                        "discord": discord,
                        "live": live,
                        "xbl": xbl,
                        "fivem": fivem,
                        "license1": license1,
                        "license2": license2,
                    }
                else:
                    if not results[key]["live"]:
                        results[key]["live"] = live
                    if not results[key]["xbl"]:
                        results[key]["xbl"] = xbl
                    if not results[key]["fivem"]:
                        results[key]["fivem"] = fivem
                    if not results[key]["license2"]:
                        results[key]["license2"] = license2
    
    if results:
        for result in results.values():
            o = f"{r}╔═══                                              ═══╗\n"
            o += f"  Name: {result['name']}\n"
            if result['discord']:
                o += f"  Discord: {result['discord']}\n"
            if result['live']:
                o += f"  Microsoft Live ID: {result['live']}\n"
            if result['xbl']:
                o += f"  Xbox Live ID: {result['xbl']}\n"
            if result['fivem']:
                o += f"  FiveM ID: {result['fivem']}\n"
            if result['license1']:
                o += f"  License1: {result['license1']}\n"
            if result['license2']:
                o += f"  License2: {result['license2']}\n"
            o += "╚═══                                              ═══╝"
            op = pystyle.Center.XCenter(o)
            print(op + "\n")
            input(f"{r}Press any key to return to the menu.")
            menu()
    else:
        error = f"[!] No information found for {s}"
        box_width = len(error) + 2

        text = f"""{r}
        ╔{'═' * box_width}╗
        {r}  {error}  {r}
        ╚{'═' * box_width}╝\n
        """
        text = pystyle.Center.XCenter(text)
        print(text + "\n")
        input(f"{r}Press any key to return to the menu.")
        menu()

url = "https://www.dropbox.com/scl/fi/5mbw8tdlqhtpi6cz2xcbu/players.7z?rlkey=v5nqm87injcmyb9lfpdaajnzk&st=mv7l7wc8&dl=1"
rarf = "players.rar"
cd = os.getcwd()
ep = cd

if not os.path.exists("players.txt"):
    print("Players.txt does not exist. Download in progress...")
    try:
        subprocess.run(f'curl -L -s -o {rarf} "{url}"', check=True, shell=True)
        print("Download completed.")
        
        print("Extraction in progress...")
        try:
            with py7zr.SevenZipFile(rarf, mode='r') as archive:
                archive.extractall(path=ep)
            print(f"Extraction completed in folder '{ep}'.")
            os.remove(rarf)
        except py7zr.exceptions.ArchiveError as e:
            print(f"Error during extraction: {e}")
        except Exception as e:
            print(f"Unexpected error during extraction: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
else:
    print(f'┌──<{pc_username}@ENFER>─[~] {y}(Enter LicenseID, DiscordID or Name)')
    s = input(f'{r}└──╼ $ {b}').lstrip("0")
    if s:
        print("")
    else:
        error = f"[!] Please specify information"
        box_width = len(error) + 2

        text = f"""{r}
        ╔{'═' * box_width}╗
        {r}  {error}  {r}
        ╚{'═' * box_width}╝\n
        """
        text = pystyle.Center.XCenter(text)
        print(text + "\n")
        input(f"{r}Press any key to return to the menu.")
        menu()

    fp = os.path.join(ep, "players.txt")
    sf(fp, s)
