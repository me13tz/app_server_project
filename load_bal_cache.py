"""
Service: The Russian Peasant's Algorithm
Architecture Includes:

- APP Computers (imported modules)
- Database --> fake_database which is the Russian Peasant algorithm
- Load Balancer algorithm

+-----+   +-----+   +-----+
| APP |   | APP |   | APP |
|  1  |   |  2  |   |  3  |
+-----+   +-----+   +-----+

"""
## IMPORT SERVERS (modules)

from random import randint

import computer1
import computer2
import computer3
import computer4


##Lists of varying lengths to test your function:
#SERVERS = ['APP_server1', 'APP_server2', 'APP_server3']

SERVERS = [computer1, computer2, computer3, computer4]

##Load Balancer algorithm:
x = len(SERVERS)
y = x + 1
s_list = SERVERS

def get_server():
    global x, y, s_list
    if y > 1:
        y -= 1
        return s_list[x - y]
    elif y == 1:
        s_list = SERVERS
        y = x
        return s_list[x - y]

##Testing Load which needs balancing
if __name__ == '__main__':
    ##simulate a number of requests:
    for i in range(21):
        ##generate some requested numbers that will hit the cache from time to time:
        z = randint(1,21)
        a = [18,21,33,55,66,77,71][z%7]
        b = [12,14,37,44,81,123,99][z%7]

        ##Run the load balancer algorithm to get us a computer
        server = get_server()
        # ##Now print the results:
        print(server.__name__)
        print(server.multiplyHandler(a,b))
        print()

