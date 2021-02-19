import logging
import asyncio

from kademlia.network import Server

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)


loop_s1 = asyncio.get_event_loop()
loop_s1.set_debug(True)

server = Server()
loop_s1.run_until_complete(server.listen(8468))

try:
    loop_s1.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.stop()
    loop_s1.close()
