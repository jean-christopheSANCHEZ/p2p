import asyncio

from kademlia.network import Server



async def run():

    # Create a node and start listening on port 8480

    node = Server()

    await node.listen(5001)

    await node.bootstrap([("0.0.0.0", 5000)])
   

    await node.set("1", "1 sur le reseau")

    await node.set("2", "2 sur le reseau")

  
    result = await node.get("1")

    print(result)

 
asyncio.run(run())
