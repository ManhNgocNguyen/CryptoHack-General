import math
from Crypto.Util.number import inverse, long_to_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with(open("D:\Python\pythonProject9\key_17a08b7040db46308f8b9a19894f9f95.pem","r"))as f:
    a = f.read()
ct = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28

n = RSA.importKey(a).n
p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
q = 77342270837753916396402614215980760127245056504361515489809293852222206596161
e = 65537
phi = (p-1) * (q-1)
d = inverse(e, phi)
key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)
print(cipher.decrypt(bytes.fromhex(hex(ct)[2:])).decode())

