import requests
import os
import pystyle
import sys
import subprocess
from colorama import init, Fore, Style

def menu():
    subprocess.run(["python", "main.py"])
    
def spn(pn):
    api_key = "UYXXd2qpcpWJ1127vT2qo7ZcILbaNnTJ"
    url = f"https://api.apilayer.com/number_verification/validate?number={pn}"
    headers = {"apikey": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if response.status_code == 200 and data['valid']:
            result = "╔═══                                                     ═══╗\n" \
                     "║  Numéro de téléphone: " + data['number'] + "                        ║\n" \
                     "   Format local: " + data['local_format'] + "\n" \
                     "   Format international: " + data['international_format'] + "\n" \
                     "   Préfixe pays: " + data['country_prefix'] + "\n" \
                     "   Code pays: " + data['country_code'] + "\n" \
                     "   Nom pays: " + data['country_name'] + "\n" \
                     "   Opérateur: " + data['carrier'] + "\n" \
                     "║  Type de ligne: " + data['line_type'] + "                                    ║\n" \
                     "╚═══                                                     ═══╝\n"
            return result
        else:
            return "Numéro de téléphone invalide ou non trouvé."
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"

pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
if __name__ == "__main__":
    print(f'\n┌──<{pc_username}@ENFER>─[~] {y}(Enter International Phone Number)')
    pn = input(f'{r}└──╼ $ {b}').lstrip("0")
    result = spn(pn)
    re = pystyle.Center.XCenter("\n" + result)
    print(r + re + "\n")
    input("Press any key to return to the menu.")
    menu()
    
