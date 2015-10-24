#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by witt on 2013-07-04.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.strxor import strxor

def decrypt_cbc(key, ciphertext):
	"""decrypt ciphertext with cbc mode"""
	message = ''
	for i in range(0, len(ciphertext)/16 - 1):
		iv = ciphertext[i*16:(i+1)*16]
		inputblock = ciphertext[(i+1)*16:(i+2)*16]
		cipher = AES.new(key, AES.MODE_CBC, iv)
		message +=cipher.decrypt(inputblock)
	if ord(message[-1]) <=16:
		message = message[:-ord(message[-1])]
	return message
	
def decrypt_ctr(key, ciphertext):
	"""decrypt ciphertext with cbc mode"""
	message = ''
	iv = ciphertext[0:16]
	for i in range(16, len(ciphertext), 16):
		inputblock = ciphertext[i:i+16]
		cipher = AES.new(key, AES.MODE_ECB)
		xorkey = cipher.encrypt(long_to_bytes(bytes_to_long(iv)+(i/16-1)))
		if len(inputblock) == 16:
			message += strxor(inputblock, xorkey)
		else:
			message += strxor(inputblock, xorkey[:len(inputblock)])
	return message


def main():
	cbckey1 = '140b41b22a29beb4061bda66b6747e14'
	cbcciphertext1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e00' + \
		'8a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
		
	cbckey2 = '140b41b22a29beb4061bda66b6747e14'
	cbcciphertext2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48'+ \
		'e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
	
	ctrkey1 = '36f18357be4dbd77f050515c73fcf9f2'
	ctrciphertext1 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc3'+\
		'88d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
	
	ctrkey2 = '36f18357be4dbd77f050515c73fcf9f2'
	ctrciphertext2 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa'\
		'0e311bde9d4e01726d3184c34451'
	
	print decrypt_cbc(cbckey1.decode('hex'), cbcciphertext1.decode('hex'))
	print decrypt_cbc(cbckey2.decode('hex'), cbcciphertext2.decode('hex'))
	print decrypt_ctr(ctrkey1.decode('hex'), ctrciphertext1.decode('hex'))
	print decrypt_ctr(ctrkey2.decode('hex'), ctrciphertext2.decode('hex'))


if __name__ == '__main__':
	main()

