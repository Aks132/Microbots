import socket
import time
import math

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.setsockopt(socket.SOL_SOCKET, 25, 'wlp0s20f3'.encode())

# sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock2.setsockopt(socket.SOL_SOCKET, 25, 'wlxd03745f1e17a'.encode())

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
#sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))
#sock2.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(6)

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
#sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('curve 200 0 0 100 -100 0 50'.encode(), 0, ('192.168.10.1', 8889))
time.sleep(7)

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
#sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('land'.encode(), 0, ('192.168.10.1', 8889))
#sock2.sendto('land'.encode(), 0, ('192.168.10.1', 8889))


