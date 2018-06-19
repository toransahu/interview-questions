import subprocess
import Crypto

command = """
uptime -p
free -m | awk 'FNR == 2 {usage= $3*100/$2} END {print usage}'
grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'
"""

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
output = process.communicate()

with open('./tmp/out.txt','w') as f:
	f.write(str(output[0],'utf8'))
