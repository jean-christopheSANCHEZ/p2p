"""
python script which read the permanentNode.conf file and launch all the permanent nodes
"""
import os
import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python permanentNode.py <name of the conf file>")
    sys.exit(1)

try: 
	f=open(sys.argv[1], "r")
	line = f.readline()
	
finally:
	f.close()

parse = line.split();
#launch servers
processServer1 = subprocess.Popen(["python3", "server1-node.py", parse[0], parse[1], parse[2]])
processServer2 = subprocess.Popen(["python3", "server2-node.py", parse[3], parse[4], parse[0], parse[1], parse[6], parse[7],parse[5]])
processServer3 = subprocess.Popen(["python3", "server3-node.py", parse[6], parse[7], parse[0], parse[1],parse[3], parse[4] ,parse[8]])

