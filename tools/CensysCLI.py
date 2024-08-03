import os
from colorama import init, Fore, Style
import subprocess
import requests
import time
import pystyle
pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
init(autoreset=True)

def menu():
    subprocess.run(["python", "main.py"])

def sd(domain):
    url = 'https://search.censys.io/api/v2/hosts/search'
    params = {
        'q': domain,
        'per_page': 50,
        'virtual_hosts': 'EXCLUDE',
        'sort': 'RELEVANCE'
    }
    headers = {
        'accept': 'application/json',
        'Authorization': 'Basic MDMwMGVkODQtYTY4ZS00MmU1LWIyZjYtYzQ2YWM3MDYzNDJlOlJLdWJaVVo0N0wyOTRCTFhCNWJmVjhQTndDOUNHUTBx'
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        ip_addresses = data['result']['hits']

        if not ip_addresses:
            print(Fore.RED + "[!] No IP addresses found.")
            return

        output_folder = os.path.join("output", "censys")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file = os.path.join(output_folder, f"{domain}-scan.txt")
        with open(output_file, "w") as file:
            file.write("=== Scan Result ===\n\n")
            file.write(f"[+] {len(ip_addresses)} results found\n\n")
            for ip_data in ip_addresses:
                ip = ip_data['ip']
                services = ip_data['services']
                file.write("[--------------------------]\n")
                file.write(f"-> IP address: {ip}\n")
                for service in services:
                    details = f"{service['extended_service_name']} (Port: {service['port']})"
                    file.write(f"{details}\n")
                file.write("[--------------------------]\n\n")

        rt = f"[+] Results file saved to: {output_file}"
        box_width = len(rt) + 2

        text = f"""{r}
        ╔{'═' * box_width}╗
        {Fore.LIGHTGREEN_EX}  {rt}  {r}
        ╚{'═' * box_width}╝\n
        """
        text = pystyle.Center.XCenter(text)
        print(text)

    else:
        et = f"[!] Error searching for {domain}"
        box_width = len(et) + 2

        text = pystyle.Center.XCenter(f"""
        ╔{'═' * box_width}╗
        {r}  {et}  {r}
        ╚{'═' * box_width}╝
        """)
        print(text)



if __name__ == "__main__":
    while True:
        print(f'\n┌──<{pc_username}@ENFER>─[~] {y}(Enter URL/IP)')
        url = input(f'{r}└──╼ $ {b}').lstrip("0")
        if url:
            try:
                sd(url)
                input("\nPress any key to return to the menu.")
                menu()
                break
            except Exception as e:
                et = f"[!] Error: {e}"
                box_width = len(et) + 2

                text = pystyle.Center.XCenter(f"""{r}
                ╔{'═' * box_width}╗
                {r}  {et}  {r}
                ╚{'═' * box_width}╝
                """)
                print(text)
                input(f"{r}Press any key to return to the menu.")
                menu()
                break
        else:
            et = "[!] Please specify IP/DOMAIN."
            box_width = len(et) + 2

            text = pystyle.Center.XCenter(f"""{r}
            ╔{'═' * box_width}╗
            {r}  {et}  {r}
            ╚{'═' * box_width}╝
            """)
            print(text)
            input(f"{r}Press any key to return to the menu.")
            menu()
            break
