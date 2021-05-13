import asyncio
from kademlia.network import Server

async def run():
    # Create a node and start listening on port 5678
    node = Server()
    await node.listen(8481)

    # Bootstrap the node by connecting to other known nodes, in this case
    # replace 123.123.123.123 with the IP of another node and optionally
    # give as many ip/port combos as you can for other nodes.
    await node.bootstrap([("0.0.0.0", 8468)])
    await node.bootstrap([("0.0.0.0", 8478)])
    

    # set a value for the key "my-key" on the network
    await node.set("3", "3 sur le reseau")

    # get the value associated with "my-key" from the network
    result = await node.get("3")
    print(result)

asyncio.run(run())
