string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

fromHex = [i for i in bytes.fromhex(string)]
for i in range(256):
    flagOrd = [i ^ o for o in fromHex]
    flagChr = "".join(chr(o) for o in flagOrd)
    if flagChr.startswith("crypto"):
        flag = flagChr
        break
print(flag)