import socket
import sys
import pyfiglet
import time
from tqdm import tqdm

print("WRITTEN BY")
pyfiglet.print_figlet("KDZsport","6x10")
print("DATE 23.08.2018\n")
print("****************************************************************")
print("START!")
print("****************************************************************\n")
def host(website):
    ip = socket.gethostbyname(website)
    return ip

if __name__ == '__main__':
    domain = sys.argv[1]
    print("################################################################")
    print("The IP address for host is:")
    print(host(domain))
    print("################################################################\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def scan(port):
    try:
        s.connect((host(domain), port))
        return True
    except:
        return False
print("Loading scaner...")
for i in tqdm(range(10)):
    time.sleep(1)

for x in range(1,10000):
    if scan(x):
        print("*Port",x,"is open!\n")

print("DONE!")