#!/usr/bin/python
# -*- coding: utf-8 -*-

blob = ''' string with same md5 hashes, differing sha256 hashes '''

from hashlib import sha256
#print sha256(blob).hexdigest()
if(sha256(blob).hexdigest()=="sha256 hash of good.py blob"): #hash of good.py blob
	print("I come in peace.")
elif(sha256(blob).hexdigest() =="sha256 hash of bad.py blob"): #hash of bad.py blob
	print("Prepare to be destroyed!")
