import hashlib
import itertools
import string
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

def hs(algo, string):
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

def bfdh(thash, algo, max_length=5):
    chars = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempt_string = ''.join(attempt)
            if hs(algo, attempt_string) == thash:
                return attempt_string
    return None

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
        et = f"[!] Invalid hash"
        box_width = len(et) + 2

        text = pystyle.Center.XCenter(f"""{r}
        ╔{'═' * box_width}╗
        {r}  {et}  {r}
        ╚{'═' * box_width}╝
        """)
        print(text)
        input(f"{r}Press any key to return to the menu.")
        menu()

        
    print(f'{r}\n┌──<{pc_username}@ENFER>─[~] {y}(Enter the hash to unhash)')
    thash = input(f'{r}└──╼ $ {b}').lstrip("0")
    if choice == '1':
        return 'md5', thash
    elif choice == '2':
        return 'sha1', thash
    elif choice == '3':
        return 'sha224', thash
    elif choice == '4':
        return 'sha256', thash
    elif choice == '5':
        return 'sha384', thash
    elif choice == '6':
        return 'sha512', thash
    elif choice == '7':
        return 'blake2b', thash
    elif choice == '8':
        return 'blake2s', thash

def main():
    algo, thash = menu1()
    if algo is None:
        et = f"[!] No algorithm selected."
        box_width = len(et) + 2

        text = pystyle.Center.XCenter(f"""
        ╔{'═' * box_width}╗
        {r}  {et}  {r}
        ╚{'═' * box_width}╝
        """)
        print(text)
        input(f"{r}Press any key to return to the menu.")
        menu()
        
    result_text = f"{y}[-] Attempting to unhash the hash '{thash}' using the {algo.upper()} algorithm..."
    box_width = len(result_text) + 2

    text = f"""{r}
    ╔{'═' * box_width}╗
      {result_text}  {r}
    ╚{'═' * box_width}╝\n
    """
    text = pystyle.Center.XCenter(text)
    print(text)

    result = bfdh(thash, algo)
    if result:
        result_text = f"{Fore.LIGHTGREEN_EX}[+] String found : {result}"
        box_width = len(result_text) - 2

        text = f"""{r}
        ╔{'═' * box_width}╗
          {result_text}  {r}
        ╚{'═' * box_width}╝\n
        """
        text = pystyle.Center.XCenter(text)
        print(text)
        input(f"{r}Press any key to return to the menu.")
        menu()
    else:
        et = f"[!] No matches found."
        box_width = len(et) + 2

        text = pystyle.Center.XCenter(f"""
        ╔{'═' * box_width}╗
        {r}  {et}  {r}
        ╚{'═' * box_width}╝
        """)
        print(text)
        input(f"{r}Press any key to return to the menu.")
        menu()
        
if __name__ == "__main__":
    main()
