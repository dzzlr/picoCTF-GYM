#!/usr/bin/python3
flag_old = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
flag = ['*' for x in range(32)]
i = 0
while i < 32:
    if i < 8:
        flag[i] = flag_old[i]
        i += 1
    elif i < 16:
        flag[i] = flag_old[23-i]
        i += 1
    elif i < 32:
        flag[i] = flag_old[46-i]
        i += 2
i = 31
while i >= 17:
    flag[i] = flag_old[i]
    i -= 2

print("picoCTF{{{}}}".format(''.join(flag)))
    
