import hashlib
import base64

def main():
    text = input('\n Input text to hash: ')
    
    #MD5
    md5 = hashlib.md5(text.encode())
    md5 = md5.hexdigest()
    print(' MD5: '+md5)
    
    #Base64
    base = base64.b64encode(bytes(f'{text}', 'utf-8'))
    base = base.decode('utf-8')
    print(' Base64: '+base)
    
    #SHA1
    sha1 = hashlib.sha1(text.encode())
    sha1 = sha1.hexdigest()
    print(' SHA1: '+sha1)
    
    #SHA256
    sha256 = hashlib.sha256(text.encode())
    sha256 = sha256.hexdigest()
    print(' SHA256: '+sha256)
    print('')
    
#    print(' 1.MD5 \n 2.Base64 \n 3.SHA1 \n 4.SHA256')
#    has = input(' [1,2,3,4]: ')
#    
#    if has == '1':
#        text = hashlib.md5(text.encode())
#        text = text.hexdigest()
#        print(' : '+text)
#    elif has == '2':
#        text = base64.b64encode(bytes(f'{text}', 'utf-8'))
#        text = text.decode('utf-8')
#        print(' : '+text)
#    elif has == '3':
#        text = hashlib.sha1(text.encode())
#        text = text.hexdigest()
#        print(' : '+text)
#    elif has == '4':
#        text = hashlib.sha256(text.encode())
#        text = text.hexdigest()
#        print(' : '+text)
#    else:
#        pass