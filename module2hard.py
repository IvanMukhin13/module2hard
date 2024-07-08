def ancient_cipher(n):
    password = ''
    for i in range(n):
        if i == 0:
            continue
        for j in range(n):
            z = i + j
            if n % z == 0 and i < j:
                password += str(i) + str(j)
    return password


number1 = ancient_cipher(6)
number2 = ancient_cipher(11)
print(number1)
print(number2)