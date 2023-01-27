# Đầu tiên mình chuyển cipher từ hex về bytes
encrypted_msg = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encrypted_msg = bytes.fromhex(encrypted_msg)
# Định dạng của flag
flag_format = b"crypto{"
# Dùng hàm zip để ghép 2 vòng lặp là 1 để xor chạy đến đây thì ra được flag là :crypto{
# %r~n-LQCn\x05AUaY6ifjtJ\x1aJMvX\x0feb\x13_l\x1eGja nên mình đoán là thiếu key nên mình cộng thêm 1 ký tự bất kỳ vào
# key thử xem thì đúng là thiếu 1 key thật khi này mình đã thu được flag chuẩn format việc cần tìm là dò đúng key nữa
# thôi
for i in range(256):
    key = [o1 ^ o2
       for (o1, o2) in zip(encrypted_msg, flag_format)] +[i]
    flag = []
    key_len = len(key)
    for i in range(len(encrypted_msg)):
        flag.append(
            encrypted_msg[i] ^ key[i % key_len]
        )
    flag = "".join(chr(o) for o in flag)
    print("Flag:", flag)
# Sau khi check thì thấy em flag: crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll} ọk nhất thì submit là xong
