#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            ��4,����Z��vO�v��V%^���#�;Ѱ�M��i���u�ť�=��T� `�Ӆ@��o|�qCV��YC�D����Q�X3�ɵ H:`h��3���I
�D<���/⚱G��=�;<"""
from hashlib import sha256
#print sha256(blob).hexdigest()
if(sha256(blob).hexdigest()=="220ad91fb8516d2879df585502d53ebce89d40a35958d866b188f585ff1f9a87"): #hash of good.py blob
	print("I come in peace.")
elif(sha256(blob).hexdigest() =="f26afca24c286908dfbf8cda163b64ea3daf4cd06d860a1faa66bc8bb6d61a5e"): #hash of bad.py blob
	print("Prepare to be destroyed!")
