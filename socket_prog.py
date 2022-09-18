import socket
import time

ur_host = "192.168.1.102"
port = 30002



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ur_host,port))

