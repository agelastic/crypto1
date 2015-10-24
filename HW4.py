import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

	# def solve_char(self, count, c0,c1):
	# 	"""docstring for solve_char"""
	# 	for i in range(0,256):
	# 		c0[-count] = chr(i ^ count)
	# 		c0[-count+1:] = 
	# 		ciphertext = (c0 + c1).decode('hex')
	# 		if query(ciphertext) return 

if __name__ == "__main__":
	po = PaddingOracle()
	str_full = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c1bdf302936266926ff37dbf7035d5eeb4".decode('hex')
	str1 = str_full[32:]
	print str1.encode('hex')
    
	for i in range(0,256):

		str2 = "a"*15+chr(ord(str1[15]) ^ i ^ 1) + str1[16:]
		print str2.encode('hex')
		print str2[15].encode('hex')
		if po.query(str2.encode('hex')):
			print "found guess",  chr(i).encode('hex')
			



