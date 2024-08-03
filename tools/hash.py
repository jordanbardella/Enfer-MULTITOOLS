import hashlib
from colorama import init, Fore, Style
import subprocess
import pystyle
import os

pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW

def menu():
    subprocess.run(["python", "main.py"])

def hash_string(algo, string):
    if algo == 'md5':
        return hashlib.md5(string.encode()).hexdigest()
    elif algo == 'sha1':
        return hashlib.sha1(string.encode()).hexdigest()
    elif algo == 'sha224':
        return hashlib.sha224(string.encode()).hexdigest()
    elif algo == 'sha256':
        return hashlib.sha256(string.encode()).hexdigest()
    elif algo == 'sha384':
        return hashlib.sha384(string.encode()).hexdigest()
    elif algo == 'sha512':
        return hashlib.sha512(string.encode()).hexdigest()
    elif algo == 'blake2b':
        return hashlib.blake2b(string.encode()).hexdigest()
    elif algo == 'blake2s':
        return hashlib.blake2s(string.encode()).hexdigest()
    else:
        raise ValueError("Unsupported algorithm")

def menu1():
    text = f"""{r}
╔═══       ═══╗
  1. MD5
  2. SHA-1
  3. SHA-224  
  4. SHA-256
  5. SHA-384
  6. SHA-512
  7. BLAKE2b
  8. BLAKE2s
╚═══       ═══╝
    """
    centertext = pystyle.Center.XCenter(text)
    print(centertext)
    print(f'{r}\n┌──<{pc_username}@ENFER>─[~] {y}(Select a hash)')
    choice = input(f'{r}└──╼ $ {b}').lstrip("0")

    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        error_text = f"[!] Invalid hash"
        box_width = len(error_text) + 2

        text = pystyle.Center.XCenter(f"""{r}
        ╔{'═' * box_width}╗
        {r}  {error_text}  {r}
        ╚{'═' * box_width}╝
        """)
        print(text)
        input(f"{r}Press any key to return to the menu.")
        menu()


    print(f'{r}\n┌──<{pc_username}@ENFER>─[~] {y}(Enter the string to hash)')
    sth = input(f'{r}└──╼ $ {b}').lstrip("0")
    if choice == '1':
        return 'md5', sth
    elif choice == '2':
        return 'sha1', sth
    elif choice == '3':
        return 'sha224', sth
    elif choice == '4':
        return 'sha256', sth
    elif choice == '5':
        return 'sha384', sth
    elif choice == '6':
        return 'sha512', sth
    elif choice == '7':
        return 'blake2b', sth
    elif choice == '8':
        return 'blake2s', sth

def main():
    algo, sth = menu1()
    if algo is None:
        error_text = f"[!] No algorithm selected."
        box_width = len(error_text) + 2

        text = pystyle.Center.XCenter(f"""
        ╔{'═' * box_width}╗
        {r}  {error_text}  {r}
        ╚{'═' * box_width}╝
        """)
        print(text)
        input(f"{r}Press any key to return to the menu.")
        menu()
    try:
        hs = hash_string(algo, sth)
        result_text = f"The {algo.upper()} hash of the string '{sth}' is: {hs}"
        box_width = len(result_text) + 2

        text = f"""{r}
        ╔{'═' * box_width}╗
          {result_text}  {r}
        ╚{'═' * box_width}╝\n
        """
        text = pystyle.Center.XCenter(text)
        print(text)
        input(f"{r}Press any key to return to the menu.")
        menu()
    except ValueError as e:
        print(e)
        input(f"{r}Press any key to return to the menu.")
        menu()
        
if __name__ == "__main__":
    main()
