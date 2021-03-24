import logging
import asyncio
import permanent
from kademlia.network import Server
import sys

if len(sys.argv) != 6:
    print("Usage: python server2-node.py <node ip> <port> <bootstrap node ip> <bootstrap port> <db file name>")
    sys.exit(1)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

async def exec():
    server = Server(storage=permanent.PermanentStorage(sys.argv[5]))
    await server.listen(int(sys.argv[2]), sys.argv[1])
    await server.bootstrap([(sys.argv[3], int(sys.argv[4]))])

    
    while True:
        await asyncio.sleep(1)
asyncio.run(exec())
