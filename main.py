#!/usr/bin/env python3

import sys
import secret_hashing as sh
import secret_crypting as sc


if __name__ == '__main__':
#    print('------SHEDMessage------')
    
    if len(sys.argv) <= 2:
        print('Usage \n>main.py <hash/encrypt/decrypt> <text_for_hash/key_for_encrypt_or_decrypt> <encrypt/decrypt  message>')
    
    
    elif sys.argv[1] == 'hash':
        sh.hash_file(sys.argv[2])
    
    
    elif sys.argv[1] == 'encrypt':
        file = open(sys.argv[3],'r')
        msg = file.read()
        encrypt = sc.encrypt(sys.argv[2], msg)
        file.close()
        file = open(sys.argv[3],'w')
        file.write(encrypt)
        print(f'Encrypted:{sys.argv[3]}')
    
    
    elif sys.argv[1] == 'decrypt':
        file = open(sys.argv[3],'r')
        msg = file.read()
        decrypt = sc.decrypt(sys.argv[2], msg)
        file.close()
        file = open(sys.argv[3],'w')
        file.write(decrypt)
        print(f'Decrypted:{sys.argv[3]}')