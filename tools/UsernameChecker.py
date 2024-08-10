import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import os
import pystyle
import json
import sys
import subprocess
from colorama import init, Fore, Style

def menu():
    subprocess.run(["python", "main.py"])

##############################################################################################################################################################################
# Twitter Username Checker Function 
##############################################################################################################################################################################

def check_twitter(username):
    url = f"https://spacesdashboard.com/u/{username}"

    headers = CaseInsensitiveDict()
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"

    resp = requests.get(url, headers=headers)

    if resp.status_code == 404:
        return f"""[0;32m[TWITTER]   : available or banned[0m"""
    else:
        return f"""[0;31m[TWITTER]   : not available[0m"""
        
##############################################################################################################################################################################
# Discord Username Checker Function 
##############################################################################################################################################################################

def check_discord(username):
    url = f"https://discord.com/api/v9/unique-username/username-suggestions-unauthed?global_name={username}"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"

    resp = requests.get(url, headers=headers)
    data = resp.json()

    if data.get("username") == username:
        return f"""[0;32m[DISCORD]   : available[0m"""
    else:
        return f"""[0;31m[DISCORD]   : not available[0m"""
        
##############################################################################################################################################################################
# Youtube Username Checker Function 
##############################################################################################################################################################################

def check_youtube(username):
    url = f"https://www.youtube.com/@{username}"
    resp = requests.get(url)

    if resp.status_code == 200:
        return f"""[0;31m[YOUTUBE]   : not available[0m"""
    else:
        return f"""[0;32m[YOUTUBE]   : available[0m"""
        
##############################################################################################################################################################################
# Github Username Checker Function 
##############################################################################################################################################################################

def check_github(username):
    base_url = "https://github.com/"

    headers = CaseInsensitiveDict()
    headers["authority"] = "github.com"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"

    user_url = base_url + username
    resp = requests.get(user_url, headers=headers)

    if resp.status_code == 404:
        return f"""[0;32m[GITHUB]    : available[0m"""
    elif resp.status_code == 200:
        return f"""[0;31m[GITHUB]    : not available[0m"""
        
##############################################################################################################################################################################
# Roblox Username Checker Function 
##############################################################################################################################################################################

def check_roblox(username):
    url = f"https://users.roblox.com/v1/usernames/users"

    headers = CaseInsensitiveDict()
    headers["authority"] = "www.tiktok.com"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"

    data = {
        "usernames": [username],
        "excludeBannedUsers": True
    }
    
    resp = requests.get(url, headers=headers, json=data)

    if "data" in resp.text:
        return f"""[0;31m[ROBLOX]    : not available[0m"""
    else:
        return f"""[0;32m[ROBLOX]    : available[0m"""
        
##############################################################################################################################################################################
# Tiktok Username Checker Function 
##############################################################################################################################################################################

def check_tiktok(username):
    url = f"https://www.tiktok.com/@{username}"

    headers = CaseInsensitiveDict()
    headers["authority"] = "www.tiktok.com"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"

    resp = requests.get(url, headers=headers)

    if "stats" in resp.text:
        return f"""[0;31m[TIKTOK]    : not available[0m"""
    else:
        return f"""[0;32m[TIKTOK]    : available[0m"""

##############################################################################################################################################################################
# Instagram Username Checker Function 
##############################################################################################################################################################################

def check_insta(username):
    sessionid = '61761726340%3AN5vEoDu5wK7vol%3A16%3AAYcEEtNSSYhp_am3aLhy7siLrmHMYCjFLqNMFJog7g'

    def get_fb_dtsg(sessionid):
        cookies = {'sessionid': sessionid}
        headers = {
            'User-Agent': 'Mozilla/5.0 ',
            'Accept': 'text/html,application/xhtml+xml',
            'Sec-Fetch-Site': 'same-origin'
        }
        try:
            fb_dtsg = requests.get('https://www.instagram.com/accounts/onetap/', cookies=cookies, headers=headers).text.split('"f":"')[1].split('","')[0]
            return fb_dtsg
        except Exception as e:
            return None

    fb_dtsg = get_fb_dtsg(sessionid)

    if fb_dtsg is not None:
        data = f"route_urls[0]=%2F{username}&routing_namespace=igx_www&__d=www&__user=0&__a=1&__req=3&__comet_req=7&fb_dtsg={fb_dtsg}"
        headers = {
            'Host': 'www.instagram.com',
            'User-Agent': 'Mozilla/5.0 ',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Sec-Fetch-Site': 'same-origin',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': f'sessionid={sessionid}',
        }

        try:
            response = requests.post('https://www.instagram.com/ajax/bulk-route-definitions/', headers=headers, data=data)

            ID = json.loads(response.text.replace("for (;;);", ""))
            ID = str(ID["payload"]["payloads"][f"/{username}"]).split("{'id': '")[1].split("', 'profile_pic_url'")[0]
            return f"""[0;31m[INSTAGRAM] : not available[0m"""
        except IndexError as index_error:
            return f"""[0;32m[INSTAGRAM] : available[0m"""
        except Exception as e:
            return f"""[0;31m[ERROR]     : {e}[0m"""
            

            
pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW

print(f'\n┌──<{pc_username}@ENFER>─[~] {y}(Enter a username)')
search = input(f'{r}└──╼ $ {b}').lstrip("0")


result1 = check_discord(search)
result2 = check_youtube(search)
result3 = check_github(search)
result4 = check_tiktok(search)
result5 = check_insta(search)
result6 = check_twitter(search)
result7 = check_roblox(search)


result = f"""{r}
╔═══                             ═══╗
  {result1}       
  {result2}
  {result3}
  {result4}
  {result5}
  {result6}
  {result7}      {r} 
╚═══                             ═══╝
"""
re = pystyle.Center.XCenter("\n" + result)
print(re + "\n")
input("Press any key to return to the menu.")
menu()
