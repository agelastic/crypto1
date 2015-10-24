def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])



def main():
	ciphertext = "ac1e37bfb15599e5f40eef805488281d".decode('hex')
	msg1 = "Pay Bob 100$"
	msg2 = "Pay Bob 500$"
	diff = strxor (msg1, msg2)
	newciph = strxor(ciphertext, diff).encode('hex')
	print newciph

if __name__ == '__main__':
	main()
