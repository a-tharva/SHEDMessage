#Encrypting
def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        if c == ' ':
            encryped.append(' ')
        else:
            key_c = ord(key[i % len(key)])
            msg_c = ord(c)
            encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

#Decrypting
def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        if c == ' ':
            msg.append(' ')
        else:
            key_c = ord(key[i % len(key)])
            enc_c = ord(c)
            msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)


def main():
    print(' \n1.Encode 2.Decode')
    choice = input('[1,2]: ')
    
    if choice == '1':
        key = input('Key:')
        msg = input('Message:')
        encrypted = encrypt(key, msg)
        print(f'Encrypted-msg:{encrypted}')
        
    elif choice == '2':
        key = input('Key:')
        msg = input('Message:')
        decrypted = decrypt(key, msg)
        print(f'Decrypted-msg:{decrypted}')
        
    else:
        pass

if __name__ == '__main__':
    main()