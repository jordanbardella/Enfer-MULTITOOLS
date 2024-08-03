import aiohttp
import asyncio
import os
from bs4 import BeautifulSoup
import subprocess
from colorama import init, Fore, Style
import pystyle

pc_username = os.getlogin()
i = 0
page_count = 0
base_url = "https://coomer.su"
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW

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
    subprocess.run(["python", "main.py"])

async def di(session, imgurl, patchf):
    global i
    async with session.get(imgurl) as response:
        if response.status == 200:
            # Ensure the directory exists
            os.makedirs(patchf, exist_ok=True)
            file_path = os.path.join(patchf, imgurl.split('/')[-1])
            with open(file_path, 'wb') as f:
                f.write(await response.read())
            i += 1
            os.system(f"title {i} - Downloaded Images - ENFER")
            rt = f"{i} - Downloaded Images | Page : [{page_count}]"
            box_width = len(rt) + 2

            text = f"""{r}
            ╔{'═' * box_width}╗
            {r}  {rt}  
            ╚{'═' * box_width}╝\n
            """
            text = pystyle.Center.XCenter(text)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii)
            print(text)

async def fu(session, url, max_a=5):
    a = 0
    while a < max_a:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
        await asyncio.sleep(2 ** a)
        a += 1
    return None

async def sup(session, uurl, patchf, npa=5):
    offset = 0

    global page_count
    alrdsp = set()
    while page_count < npa:
        purl = f"{uurl}?o={offset}"
        user_response = await fu(session, purl)
        if user_response:
            user_soup = BeautifulSoup(user_response, 'html.parser')
            post_links = user_soup.find_all('a', href=lambda href: href and "/post/" in href)
            cpp = {f"{base_url}{link.get('href')}" for link in post_links}
            if cpp.issubset(alrdsp):
                break
            alrdsp.update(cpp)
            for link in post_links:
                pu = f"{base_url}{link.get('href')}"
                pr = await fu(session, pu)
                if pr:
                    post_soup = BeautifulSoup(pr, 'html.parser')
                    images = post_soup.find_all('img', attrs={'data-src': lambda src: src and src.startswith("//img.coomer.su/thumbnail")})
                    for img in images:
                        imgurl = f"https:{img['data-src']}"
                        await di(session, imgurl, patchf)
            offset += 50
            page_count += 1
        else:
            break

async def main():
    print(f'\n┌──<{pc_username}@ENFER>─[~] {y}(Enter a OF Username)')
    username = input(f'{r}└──╼ $ {b}').lstrip("0")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ascii)
    print(f'\n┌──<{pc_username}@ENFER>─[~] {y}(Please specify the number of pages you would like to scrape)')
    pages = input(f'{r}└──╼ $ {b}').lstrip("0")
    npa = float('inf') if pages == 'all' else int(pages)
    suffix = 'all' if pages == 'all' else f"{pages}p"
    
    dir = "output/scrapeof"
    patchf = os.path.join(dir, username)
    os.makedirs(patchf, exist_ok=True)
    
    uurl = f"https://coomer.su/onlyfans/user/{username}"
    async with aiohttp.ClientSession() as session:
        response = await session.get(uurl, allow_redirects=False)
        if response.status in (301, 302) and 'artists' in response.headers.get('Location', ''):
            api_url = "https://coomer.su/api/v1/creators"
            api_response = await session.get(api_url)
            if api_response.status == 200:
                creators_data = await api_response.json()
                matching_creators = [creator for creator in creators_data if username.lower() in creator['name'].lower()]
                if matching_creators:
                    if len(matching_creators) > 10:
                        rt = f"Too many results, please refine your request."
                        box_width = len(rt) + 2

                        text = f"""{r}
                        ╔{'═' * box_width}╗
                        {r}  {rt}  
                        ╚{'═' * box_width}╝\n
                        """
                        text = pystyle.Center.XCenter(text)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(ascii)
                        print(text)
                        input("\nPress any key to return to the menu.")
                        menu()
                        return
                    results_description = "\n".join([f"{creator['name']} - {creator['service']}" for creator in matching_creators])
                    print("Results found :\n" + results_description)
                else:
                    rt = f"No users matching {username} found."
                    box_width = len(rt) + 2

                    text = f"""{r}
                    ╔{'═' * box_width}╗
                    {r}  {rt}  
                    ╚{'═' * box_width}╝\n
                    """
                    text = pystyle.Center.XCenter(text)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(ascii)
                    print(text)
                    input("\nPress any key to return to the menu.")
                    menu()
                return
            else:
                rt = f"API error: Failed to retrieve data from the API."
                box_width = len(rt) + 2

                text = f"""{r}
                ╔{'═' * box_width}╗
                {r}  {rt}  
                ╚{'═' * box_width}╝\n
                """
                text = pystyle.Center.XCenter(text)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(ascii)
                print(text)
                input("\nPress any key to return to the menu.")
                menu()
            return
        else:
            await sup(session, uurl, patchf, npa)

            rt = f"Scraping finished for {username}."
            box_width = len(rt) + 2

            text = f"""{r}
            ╔{'═' * box_width}╗
            {r}  {rt}  
            ╚{'═' * box_width}╝\n
            """
            text = pystyle.Center.XCenter(text)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii)
            print(text)
            input("\nPress any key to return to the menu.")
            menu()
            
if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}")
        input("\nPress any key to return to the menu.")
        menu()
