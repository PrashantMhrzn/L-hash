# L-hash
Like a hasher

## About
L-hash(Like a hasher) is a python program that acts as an oversimplified hashing algorithm. It encrypts and decrypts any file you give it. 

## Requirements
L-hash requires Python3 on the device.

## Installation

Clone the Repository;
```bash
$ git clone https://github.com/PrashantMhrzn/L-hash.git
```

CD into the cloned directory;
```bash
$ cd L-hash/
```

Run Lhash.py;
```
$ python3 Lhash.py -e raw.txt
$ python3 Lhash.py -d encoded.txt
```
## Usage
```
$python3 Lhash.py [-e for encrypt/-d for decrypt] [file name]

$ python3 Lhash.py -h
usage: Lhash.py [-h] [-e] [-d]

Encrypt or decrypt a file

optional arguments:
  -h, --help            show this help message and exit
  -e , --encrypt_file   file you want to encrypt
  -d , --decrypt_file   file you want to decrypt
 
```
##Example
```
$ python3 Lhash.py -e raw.txt    
File encrypted as encoded.txt
$ python3 Lhash.py -d encoded.txt
File decrypted as decoded.txt
```
Before:
![alt text](https://github.com/PrashantMhrzn/L-hash/blob/main/SS/1.PNG)
![alt text](https://github.com/PrashantMhrzn/L-hash/blob/main/SS/2.PNG)

After:
![alt text](https://github.com/PrashantMhrzn/L-hash/blob/main/SS/3.PNG)


## Liscense
[GNU](https://github.com/PrashantMhrzn/L-hash/blob/main/LICENSE)
