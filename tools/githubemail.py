import requests
import os
from colorama import init, Fore, Style
import subprocess
import pystyle


pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW

def menu():
    subprocess.run(["python", "main.py"])

print(f'{r}┌──<{pc_username}@ENFER>─[~] {y}(Enter Username)')
username = input(f'└──╼ $ {b}').lstrip("0")
url = f"https://api.github.com/users/{username}/events/public"
response = requests.get(url)

if response.status_code == 200:
    events = response.json()
    emails = set()

    for event in events:
        if 'payload' in event and 'commits' in event['payload']:
            for commit in event['payload']['commits']:
                if 'author' in commit and 'email' in commit['author']:
                    email = commit['author']['email']
                    if '@users.noreply.github.com' not in email:
                        emails.add(email)
    if emails:
        emails_list = "".join(emails)
        text = f"{Fore.LIGHTGREEN_EX}[+] Email found: {emails_list}"
    else:
        text = f"{r}[!] No emails found"
        
    box_width = len(text) - 2

    text = pystyle.Center.XCenter(f"""{r}
    ╔{'═' * box_width}╗
      {text}  {r}
    ╚{'═' * box_width}╝
    """)
    print(text)
    input(f"{r}Press any key to return to the menu.")
    menu()
else:
    et = f"[!] ERROR : {response.status_code}"
    box_width = len(et) + 2

    text = pystyle.Center.XCenter(f"""
    ╔{'═' * box_width}╗
    {r}  {et}  {r}
    ╚{'═' * box_width}╝
    """)
    print(text)
    input(f"{r}Press any key to return to the menu.")
    menu()
