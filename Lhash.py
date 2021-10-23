import argparse
from encrypter import encrypt
from decrypter import decrypt


parser = argparse.ArgumentParser(description='Encrypt or decrypt a file')
parser.add_argument('-e', '--encrypt_file', metavar='',help='file you want to encrypt')
parser.add_argument('-d', '--decrypt_file', metavar='',help='file you want to decrypt')
args = parser.parse_args()


if args.encrypt_file:
    with open(args.encrypt_file, 'r') as raw_file:
        raw = raw_file.read()

    raw_lst = [char for char in raw]

    with open('encoded.txt', 'w') as f:
        f.write(encrypt(raw_lst))
    
    print('File encrypted as encoded.txt')

if args.decrypt_file:
    with open(args.decrypt_file, 'r') as raw_file:
        raw = raw_file.read()

    raw_lst = [char for char in raw]

    with open('decoded.txt', 'w') as f:
        f.write(decrypt(raw_lst))

    print('File decrypted as decoded.txt')
    
