"""
python script which read the permanentNode.conf file and launch all the permanent nodes
"""
import os
import subprocess

try: 
	f=open("permanentNode.conf", "r")
	line = f.readline()
	
finally:
	f.close()

parse = line.split();
#launch servers
processServer1 = subprocess.Popen(["python3", "server1-node.py", parse[0], parse[1], parse[2]])
processServer2 = subprocess.Popen(["python3", "server2-node.py", parse[3], parse[4], parse[0], parse[1], parse[5]])
processServer3 = subprocess.Popen(["python3", "server3-node.py", parse[6], parse[7], parse[0], parse[1], parse[8]])

