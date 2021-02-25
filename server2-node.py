import logging
import asyncio
import sys

from kademlia.network import Server

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

async def exec():
    server = Server()
    await server.listen(5002)
    await server.bootstrap([("0.0.0.0", 5000)])

    
    while True:
        await asyncio.sleep(1)
asyncio.run(exec())
