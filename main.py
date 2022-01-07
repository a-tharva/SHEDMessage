#!/usr/bin/env python3

import sys
import secret_hashing as sh
import secret_crypting as sc


if __name__ == '__main__':
    print('------(SHEDM)essage------')
    
    if len(sys.argv) < 2:
        print('Usage main.py <hash/encrypt/decrypt> <text_for_hash/key_for_encrypt_or_decrypt> <encrypt/decrypt_message>')
    
    elif sys.argv[1] == 'hash':
        sh.main(sys.argv[2])
    
    elif sys.argv[1] == 'encrypt':
        encrypted = sc.encrypt(sys.argv[2], ' '.join(sys.argv[3:]))
        print(f'Encrypted-msg:{encrypted}')
        
    elif sys.argv[1] == 'decrypt':
        decrypted = sc.decrypt(sys.argv[2], ' '.join(sys.argv[3:]))
        print(f'Decrypted-msg:{decrypted}')