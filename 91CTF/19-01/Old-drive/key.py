#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Distributed under terms of the MIT license.
#
from base64 import*
import hashlib
flag = ''
key1='\xf2\xee\xef\xf5\xd9\xef'
key2='\x63\x31\x39\x7a\x62\x57\x4e\x66'
key3='waaaaawwwww22222qqqaaw'

for i in key1:
    flag+=chr(ord(i)^0x86)

flag += b64decode(key2)

flag += key3

print "flag{%s}"%flag
print hashlib.md5(flag).hexdigest()
