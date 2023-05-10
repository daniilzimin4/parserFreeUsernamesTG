from pyrogram import Client
from pyrogram.raw import functions
import asyncio
import requests
from bs4 import BeautifulSoup
from time import sleep
from config import *

# Get 5000 most popular words in english
x = BeautifulSoup(requests.get('https://studynow.ru/dicta/allwords').text, "html.parser")
y = x.text.split("\n")
z = []
for i in y:
    if i != "" and '0' <= i[0] <= '9' and not i.count('5000'):
        tmp = ""
        for j in i:
            if "a" <= j <= "z":
                tmp += j
        if len(tmp) >= 5:
            z.append(tmp)
print(z)


# Checker for each word
async def test():
    async with Client("my_account2", api_id=configID, api_hash=configHASH) as app:
        for i in z:

            try:
                r = await app.invoke(
                    functions.account.CheckUsername(
                        username=i
                    )
                )
                if r:
                    print(str(r) + " " + i)
            except:
                '400 USERNAME_INVALID'
            sleep(5)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
    loop.close()


if __name__ == '__main__':
    main()
