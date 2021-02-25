import asyncio

from kademlia.network import Server



async def run():

    # Create a node and start listening on port 8480

    node = Server()

    await node.listen(5001)

    # Bootstrap the node by connecting to other known nodes, in this case

    # replace 123.123.123.123 with the IP of another node and optionally

    # give as many ip/port combos as you can for other nodes.

    #await node.bootstrap([("0.0.0.0", 5001)])

    await node.bootstrap([("0.0.0.0", 5000)])
    #await node.bootstrap([("0.0.0.0", 8478)])
    # set a value for the key "my-key" on the network

    await node.set("1", "1 sur le reseau")

    await node.set("2", "2 sur le reseau")

    # get the value associated with "my-key" from the network

    result = await node.get("1")

    print(result)

    #try:

    #    loop_s2.run_forever()

    #except KeyboardInterrupt:

    #    pass

    #finally:

    #   server.stop()

    #    loop_s2.close()

asyncio.run(run())
