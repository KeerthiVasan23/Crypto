# Crypto

# -----ROT.py-----
Custom .py script to encrypt or decrypt ROT-n ciphers. Decrypt even without knowing key(i.e n).

## Requirments and/or Dependencies:
pyenchant -python spellchecking library

_As stated in official documentation python 3.0 is intentionally backwards incompatible_
https://docs.python.org/release/3.0.1/whatsnew/3.0.html 

### To avoid dependency issues :
(run below commands in linux terminal)

sudo apt install python3-pip   
pip3 install pyEnchant

NOTE:
$ ROT-13 applied twice will yields same text
$ To decrypt without knowing key, cipher text must yeild a valid english text
$ ROT-n virtually provides no cryptographic security
