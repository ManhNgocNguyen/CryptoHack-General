#!/usr/bin/env python3

import time
from Crypto.Util.number import long_to_bytes
import hashlib
import json
from socket import *


serverName = 'socket.cryptohack.org'
serverPort = 13372
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((serverName, serverPort))
msg = sock.recv(100)
print(msg.decode('utf-8'))

def generate_key(time):
    current_time = time
    key = long_to_bytes(current_time)
    return hashlib.sha256(key).digest()


def encrypt(ct, key):
    assert len(ct) <= len(key)
    ciphertext = b''
    for i in range(len(ct)):
        ciphertext += bytes([ct[i] ^ key[i]])
    return ciphertext.hex()


def get_ciphertext(sock):
    get_flag = {"option":"get_flag"}
    json_get_flag = (json.dumps(get_flag) + '\n').encode()
    sock.send(json_get_flag)
    json_ciphertext = sock.recv(100)
    return json.loads(json_ciphertext)['encrypted_flag']


ciphertext = bytes.fromhex(get_ciphertext(sock))
curr_time = int(time.time())

for addition_time in range(10): # Đoạn này là do cái thời gian khởi tạo ban đầu so với thời gian  chạy thuật toán
                                    # đến lúc tính khóa nó chênh nhau 1 khoảng mà theo code thời gian đó tính số nguyên
                                    # nên mình cứ chạy tầm trong khoảng là 10 là thỏa mãi
                                    # Còn về giải mãi thì cái này mình dùng json lấy bản bị mã khóa xor với cái key là ra
    key = generate_key(curr_time - addition_time)
    plaintext = bytes.fromhex(encrypt(ciphertext, key))
    if b'crypto{' in plaintext:
        print(plaintext)

sock.close()
