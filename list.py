import asyncio
import aiohttp  # pip install aiohttp aiodns
import time
from bs4 import BeautifulSoup
import urllib.request,requests,json
from random import randrange
i=0
#api_key = "Tg Api Key here"
#chat_id = "Tg chat id here"
#ennter =input("start page: ")
rand=randrange(345234523452345234523452345)
async def get(
    session: aiohttp.ClientSession,
    add: str,
    **kwargs
) -> dict:
    global i
    url = f"https://blockchain.info/address/{add}?format=json"
    try:
        resp = await session.request('GET', url=url, **kwargs)
        data = await resp.json(content_type=None)
        bal=data['n_tx']
        print(i,"-   Transactions for " + add + " : " + str(data['n_tx']))
        i+=1
        if bal > 0:
            loot = "Collision found at address: "+add+"\nPage no. :"+str(rand)+"\n"
            print (loot)
            print ("Writing to loot.txt...")
            lootxt = open("loot.txt", 'a')
            lootxt.write(loot)
            lootxt.close()

        return data
    except asyncio.TimeoutError:
            pass
    except Exception as e:
            print("Error: "+repr(e))


async def main(arr, **kwargs):
    global i
    async with aiohttp.ClientSession() as session:
        tasks = []
        for a in arr:
            tasks.append(get(session=session, add=a, **kwargs))
        htmls = await asyncio.gather(*tasks, return_exceptions=False)
        return htmls

if __name__ == '__main__':
    n=0
    while True:
        arr = []
        try:          
            URL = 'http://localhost:8085/'+str(rand)
            page = requests.get(URL)
            priv=[]
            pub=[]
            pub2=[]
            print("Page no. :",rand)
            print("\n\n--------------------------------------------\n\n")
            soup = BeautifulSoup(page.content, 'html.parser')
            for each_span in soup.findAll('span'):
                address=each_span.text
                row=address.split()
                if n%2==0:
                    priv.append(row[1])
                    pub.append(row[2])
                    pub2.append(row[3])
                n+=1
            for item in pub:    
                arr.append(item)
            for item in pub2:
                arr.append(item)
            rand+=1
        except Exception as e:
            print("Error: "+repr(e))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(arr))
