import logging
import asyncio

from kademlia.network import Server
from kademlia.crawling import RPCFindResponse

import sys

if len(sys.argv) != 5:
    print("Usage: python server3-node.py <node ip> <port> <bootstrap node ip> <bootstrap port>")
    sys.exit(1)


handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

async def exec():
    server = Server()
    await server.listen(int(sys.argv[2]), sys.argv[1])
    await server.bootstrap([(sys.argv[3], int(sys.argv[4]))])
    
    #list_node = RPCFindResponse([(0,0)])
    #list_node.get_node_list()

    
    while True:
        await asyncio.sleep(1)
asyncio.run(exec())
