#!/usr/bin/python
from Crypto.Cipher import AES
from Crypto.Hash import MD5
from glob import glob
import re

for name in glob('/bin/*'):
  with open(name, 'rb') as f:
    md5 = MD5.new()
    md5.update(f.read())

  aes_e = AES.new(md5.digest(), AES.MODE_CBC, 'ThisIsRandomLOL!')
  flag = "489917cd3093786a6f1eb81645373a51dc1594cad896b2352f3be3c2dacbef00f9621542cda23826b1e77719207b53e9".decode("hex")

  str = aes_e.decrypt(flag)
  if not re.compile(r'[^\x20-\x80]').search(str):
    print "klu
