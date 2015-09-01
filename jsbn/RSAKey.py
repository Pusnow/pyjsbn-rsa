# -*- coding: utf8 -*-
from rsa import key, encrypt, decrypt, PublicKey, PrivateKey, newkeys


class RSAKey :

	#"empty" RSA key constructor
	def __init__ (self):
		self.n = None
		self.e = 0
		self.d = None
		self.p = None
		self.q = None
		self.dmp1 = None
		self.dmq1 = None
		self.coeff = None


	#Set the public key fields N and e from hex strings
	def SetPublic(self,N,E):
		if N != None and E != None and len(N) > 0 and len(E) > 0:
			self.n = int(N,16)
			self.e = int(E,16)
		else :
			raise ValueError 


	#Return the PKCS#1 RSA encryption of "text" as an even-length hex string
	def Encrypt(self, text):
		if text == None:
			return None

		pubkey = PublicKey(self.n, self.e)
		ciphertext = encrypt(text,pubkey)
		return ''.join([("%x"% ord(x)).zfill(2) for x in ciphertext])


	#Set the private key fields N, e, and d from hex strings
	def SetPrivate(self,N,E,D) :
		if N != None and E != None and len(N) > 0 and len(E) > 0 :
			self.n = int(N,16)
			self.e = int(E,16)
			self.d = int(D,16)
		else :
			raise ValueError 


	#Set the private key fields N, e, d and CRT params from hex strings
	def SetPrivateEx(self,N,E,D,P,Q,DP,DQ,C):
		if N != None and E != None and len(N) > 0 and len(E) > 0 :
			self.n = int(N,16)
			self.e = int(E,16)
			self.d = int(D,16)
			self.p = int(P,16)
			self.q = int(Q,16)
			self.dmp1 = int(DP,16)
			self.dmq1 = int(DQ,16)
			self.coeff = int(C,16)

		else: 
			raise ValueError 

	# Return the PKCS#1 RSA decryption of "ctext".
	# "ctext" is an even-length hex string and the output is a plain string.
	def Decrypt(self, ctext) :
		import re
		ctext = ''.join([chr(int(x, 16)) for x in re.findall(r'\w\w', ctext)])
		#c = int(ctext,16)
		prikey = PrivateKey(self.n, self.e, self.d, self.p, self.q, self.dmp1, self.dmq1, self.coeff)
		return decrypt(ctext,prikey)


	#Generate a new random private key B bits long, using public expt E
	def Generate (self,B,E):
		self.e = int(E,16)
		(pubkey, prikey) = newkeys(B)
		self.n = pubkey.n
		self.e = pubkey.e
		self.d = prikey.d
		self.p = prikey.p
		self.q = prikey.q
		self.dmp1 = prikey.exp1
		self.dmq1 = prikey.exp2
		self.coeff = prikey.coef

		






