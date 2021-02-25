import logging
import asyncio

from kademlia.network import Server
from kademlia.crawling import RPCFindResponse

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

async def exec():
    server = Server()
    await server.listen(5003)
    await server.bootstrap([("0.0.0.0", 5000)])
    
    #list_node = RPCFindResponse([(0,0)])
    #list_node.get_node_list()

    
    while True:
        await asyncio.sleep(1)
asyncio.run(exec())
