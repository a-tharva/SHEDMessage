import hashlib


BUF_SIZE = 65536


md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()


def hash_file(filename):
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha256.update(data)
    
    print(f'MD5: {md5.hexdigest()}')
    print(f'SHA1: {sha1.hexdigest()}')
    print(f'SHA256: {sha256.hexdigest()}')
