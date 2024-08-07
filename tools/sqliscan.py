import requests
import os
import sys
import subprocess
import pystyle 
from colorama import init, Fore, Style

pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW

def menu():
    subprocess.run(["python", "main.py"])

def csqli(url):
    iturl = url + "'"
    try:
        response = requests.get(iturl, timeout=5)
        content = response.text.lower()

        sqlerr = [
            "you have an error in your sql syntax",
            "warning: mysql",
            "unclosed quotation mark",
            "quoted string not properly terminated",
            "sqlstate[42000]",
            "syntax error",
            "unterminated string constant",
            "syntax error near",
            "unexpected end of SQL command",
            "no such table",
            "unknown column",
            "where clause",
            "incorrect syntax near",
            "could not find driver",
            "microsoft sql native client error",
            "odbc sql server driver",
            "syntax error in string",
            "mysql server version for the right syntax",
            "check the manual that corresponds to your",
            "not a valid MySQL result resource",
            "pg_query()",
            "pg_exec()",
            "sql syntax error",
            "division by zero",
            "column count doesn't match value count at row",
            "unrecognized token",
            "invalid use of group function",
            "sql error or missing database",
            "unable to prepare statement",
            "subquery returned more than 1 value",
            "missing right parenthesis",
            "ora-00933: sql command not properly ended",
            "ora-00936: missing expression",
            "ora-00907: missing right parenthesis",
            "ora-01756: quoted string not properly terminated",
            "sqlcmd: error",
            "conversion failed when converting",
            "the select list for the insert statement contains fewer items",
            "incorrect integer value",
            "conversion failed when converting the varchar value",
            "sql logic error",
            "sqlite error",
            "syntax error or access violation",
            "ora-00942: table or view does not exist",
            "invalid identifier",
            "bad sql grammar",
            "mysql syntax error",
            "no data found",
            "numeric or value error",
            "invalid character value for cast specification",
            "dynamic sql error",
            "ambiguous column name",
            "object required",
            "unclosed quotation mark after the character string",
            "data truncation",
            "failed to execute sql statement",
            "invalid object name",
            "missing data source name",
            "too few parameters. expected",
            "result consists of more than one row",
            "duplicate entry",
            "null value in column violates not-null constraint",
            "duplicate key value violates unique constraint",
            "foreign key constraint fails",
            "violates foreign key constraint",
            "cannot insert the value null",
            "integrity constraint violation",
            "unique constraint violated",
            "cannot insert duplicate key",
            "primary key must be unique",
            "maximum recursion depth exceeded",
            "cannot convert character string",
            "illegal mix of collations",
            "illegal mix of collations for operation",
            "no query specified",
            "relation does not exist",
            "invalid cursor state",
            "division by zero",
            "timeout expired",
            "network error"
        ]
        
        if any(error in content for error in sqlerr):
            message = f"Valid : {url}"
        else:
            message = f"Not Valid : {url}"
    except requests.RequestException as e:
        message = f"Not Valid : {url} (Error during request : {e})"
        
    box_width = len(message) + 4
    top_border = f"{r}╔{'═' * (box_width - 2)}╗"
    bottom_border = f"╚{'═' * (box_width - 2)}╝"
    padded_message = f"║ {message} ║"

    output = f"{top_border}\n{padded_message}\n{bottom_border}"
    output = pystyle.Center.XCenter(output)
    return output


def main():
    print(f'\n┌──<{pc_username}@ENFER>─[~] {y}(Enter URL)')
    url = input(f'{r}└──╼ $ {b}').strip()

    if url:
        result = csqli(url)
        print("\n" + result)

    else:
        print(r + "No URL provided" + Style.RESET_ALL)

if __name__ == "__main__":
    try:
        main()
        input("\n" + r + "Press any key to return to the menu.")
        menu()
    except KeyboardInterrupt:
        clear()
        print(Fore.RED + "\nExiting..." + Style.RESET_ALL)
        sys.exit(0)
