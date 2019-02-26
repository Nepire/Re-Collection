#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Distributed under terms of the MIT license.
# Author = nepire
#
key = "access denieda"
key1 = ""
flag = ""

for i in range(len(key)):
    key1 += chr(ord(key[i])^i)

for i in range(len(key)):
    if i%3==0:
        flag += chr(ord(key1[i])^31)
    elif i%3==1:
        flag += chr(ord(key1[i])^32)
    elif i%3==2:
        flag += chr(ord(key1[i])^33)

