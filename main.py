import asyncio
import aiohttp
import time

from bs4 import BeautifulSoup
import urllib.request, requests, json
from random import randrange
i = 0
# rand=randrange(904625697166532776746648320380374280061136459335199598625340549132850298880, 904625697166532776746648320380374280100293470930272690489102837043110636675) # END
# rand=randrange(288230376151711744, 904625697166532776746648320380374280100293470930272690489102837043110636675) #66x256
rand = randrange(10000000000000000000000000)
# rand=randrange(11417981541647679048466287755595961091061972992) # 160
# rand=randrange(288230376151711744, 11417981541647679048466287755595961091061972992) # 66x160
# rand=randrange(144115188075855872, 5708990770823839524233143877797980545530986496) # 66x160_https://bitcoindirectory.me/
# rand=randrange(18889465931478580854784) # 80
# rand=randrange(9444732965739290427392, 18889465931478580854784) # 80
# rand=randrange(288230376151711744, 576460752303423488) # 66
# rand=randrange(848086591093624478199982800356600887597192270500297099898370976620457492480, 904625697166532776746648320380374280100293470930272690489102837043110636672) # F
# rand=randrange(56539106072908298546665520023773392506479484700019806659891398441363832832, 113078212145816597093331040047546785012958969400039613319782796882727665664) # 1
async def get(
        session: aiohttp.ClientSession,
        add: str,
        **kwargs
) -> dict:
    global i
    url = f"https://blockchain.info/address/{add}?format=json&limit=10"
    try:
        resp = await session.request('GET', url=url, **kwargs, timeout=30)
        data = await resp.json(content_type=None)
        bal = data['n_tx']
        print(i, "-   Transactions to address: " + add + " : " + str(data['n_tx']))
        i += 1
        if bal > 0:
            loot = "Found  address: " + add + "\nPage no. :" + str(rand) + "\n"
            print(loot)
            print("Writing to loot.txt...")
            lootxt = open("loot.txt", 'a')
            lootxt.write(loot)
            winsound.Beep(frequency, duration)
            lootxt.close()
        return data
    except asyncio.TimeoutError:
        pass
    except Exception as e:
        print("Oops: " + repr(e))


async def main(arr, **kwargs):
    global i
    async with aiohttp.ClientSession() as session:
        tasks = []
        for a in arr:
            tasks.append(get(session=session, add=a, **kwargs))
        htmls = await asyncio.gather(*tasks, return_exceptions=False)
        return htmls


if __name__ == '__main__':
    n = 0
    while True:
        arr = []
        try:
            URL = 'https://lbc.cryptoguru.org/dio/' + str(rand)
            # URL = 'https://bitcoindirectory.me/'+str(rand)
            page = requests.get(URL)
            priv = []
            pub = []
            pub2 = []
            print("Page:"  , rand)
            print("\n\n=========================================================\n\n")
            soup = BeautifulSoup(page.content, 'html.parser')
            for each_span in soup.findAll('span'):
                address = each_span.text
                row = address.split()
                if n % 2 == 0:
                    priv.append(row[1])
                    pub.append(row[2])
                    pub2.append(row[3])
                n += 1
            for item in pub:
                arr.append(item)
            for item in pub2:
                arr.append(item)
            rand += 1
            time.sleep(10)
        except Exception as e:
            print("Error: " + repr(e))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(arr))
