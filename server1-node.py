import logging
import asyncio
import permanent
from kademlia.network import Server
import kademlia
import sys


if len(sys.argv) != 3:
    print("Usage: python server1-node.py <node ip> <port>")
    sys.exit(1)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)


loop_s1 = asyncio.get_event_loop()
loop_s1.set_debug(True)
server = Server(storage=permanent.PermanentStorage())
loop_s1.run_until_complete(server.listen(int(sys.argv[2]), sys.argv[1]))


try:
    loop_s1.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.stop()
    loop_s1.close()
