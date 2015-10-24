#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by witt on 2013-07-04.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from Crypto.Hash import SHA256 

def get_h0(filename):
	"""docstring for get_h0"""
	with open(filename, 'r') as content_file:
	    content = content_file.read()
	curr_hash = ""
	print len(content)
	for i in range (len(content)/1024, -1, -1):
		hashobj = SHA256.new(content[i*1024:(i+1)*1024] + curr_hash)
		curr_hash = hashobj.digest()
	return curr_hash
	


def main():
	print get_h0('/Users/witt/Virtualenvs/crypto1/file1.mp4').encode('hex')
	print get_h0('/Users/witt/Virtualenvs/crypto1/file2.mp4').encode('hex')
	
if __name__ == '__main__':
	main()

