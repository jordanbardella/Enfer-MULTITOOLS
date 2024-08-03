import requests
from bs4 import BeautifulSoup
import json
import re
import os
import subprocess
import pystyle
from colorama import Fore, init

init(autoreset=True)
pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW

def menu():
    subprocess.run(["python", "main.py"])

def check(ip):
    url = f"https://www.shodan.io/host/{ip}"
    resp = requests.get(url)
    hc = resp.text
    soup = BeautifulSoup(hc, 'html.parser')

    st = soup.find('script', text=re.compile('const VULNS'))

    if st:
        sc = st.string

        jsd = re.search(r'const VULNS = ({.*?});', sc)
        if jsd:
            jsdata = jsd.group(1)
            
            vulnerabilities = json.loads(jsdata)
            data = []

            for cve, details in vulnerabilities.items():
                data.append([cve, ', '.join(map(str, details['ports']))])

            sr(ip, vulnerabilities)
            
            return data
    return None

def sr(ip, vulnerabilities):
    dir = 'output\\cvescan'

    os.makedirs(dir, exist_ok=True)

    file_path = os.path.join(dir, f'{ip}_vulnerabilities.json')

    with open(file_path, 'w') as f:
        json.dump(vulnerabilities, f, indent=4)
    
    result_text = f"[+] Results saved to: {file_path}"
    box_width = len(result_text) + 2

    text = f"""{r}
    ╔{'═' * box_width}╗ 
    {Fore.LIGHTGREEN_EX}  {result_text}  {r}
    ╚{'═' * box_width}╝
    """
    text = pystyle.Center.XCenter(text)
    print(text)

print(f'\n┌──<{pc_username}@ENFER>─[~] {y}(Enter domain/ip)')
ip = input(f'{r}└──╼ $ {b}').lstrip("0")
result = check(ip)
if result:
    print("")
else:
    ncvet = "[-] No CVE FOUND"
    box_width = len(ncvet) + 2  

    text = f"""{r}
    ╔{'═' * box_width}╗ 
    {Fore.YELLOW}  {ncvet}  {r}
    ╚{'═' * box_width}╝
    """
    text = pystyle.Center.XCenter(text)
    print(text)

input(f"Press any key to return to the menu.")
menu()
