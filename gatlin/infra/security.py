import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

import gatlin.config.configLocation as loc

PRIVATE_KEY = 0
PUBLIC_KEY = 0


# 废弃，用于生成RSA密钥对
def create_rsa_key():
    key = RSA.generate(1024)
    encrypted_key = key.exportKey(pkcs=8, protection="scryptAndAES128-CBC")
    # encrypted_key = key.exportKey(pkcs=1)
    print('encrypted_key:', encrypted_key)
    with open("PH_DEV/my_private_rsa_key.pem", "wb") as f:
        f.write(encrypted_key)
    with open("PH_DEV/my_rsa_public.pem", "wb") as f:
        f.write(key.publickey().exportKey())


def init(ENV):
    global PRIVATE_KEY
    global PUBLIC_KEY
    # 小心相对路径的读写，infra包访问上级目录要替换位置
    pubKeyPemFile = loc.get_location() + "/" + ENV + "/" + "qihoo360-publicKey.pem"
    pvtKeyPemFile = loc.get_location() + "/" + ENV + "/" + "qihoo360-privateKey.pem"
    with open(pubKeyPemFile) as ppf:
        PUBLIC_KEY = RSA.import_key(ppf.read())
    with open(pvtKeyPemFile) as pkf:
        encoded_key = pkf.read()
    PRIVATE_KEY = RSA.import_key(encoded_key)


def encrypt(raw):
    cipher_rsa = PKCS1_v1_5.new(PUBLIC_KEY)
    en_data = base64.b64encode(cipher_rsa.encrypt(raw))
    return en_data


def decrypt(enc):
    cipher_rsa = PKCS1_v1_5.new(PRIVATE_KEY)
    data = cipher_rsa.decrypt(base64.b64decode(enc), None)
    return data


if __name__ == '__main__':
    init('PH_DEV')
    xx = encrypt(b"hahha")
    print(str(xx, 'utf-8'))
    yy = decrypt(xx)
    print(str(yy, 'utf-8'))
