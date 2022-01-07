import hashlib
import base64

def main(text):
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
    
    
if __name__ == '__main__':
    text = input('\n Input text to hash: ')
    main(text)