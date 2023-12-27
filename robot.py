# Training the modified YOLO-V7 for occlusion aware Robot-vision 
# Written and Tested By: Sheekar Banerjee
# Supervised By: Dr. Humayun Kabir
# Inha University, South Korea

import socket
import time

HEADERSIZE = 1000

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 2000)) # PORT=2000

while True:

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(1000)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False


        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg received")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''

print(full_msg)