# -*- coding: utf8 -*-
from rsa import key, encrypt, PublicKey


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
			self.pubkey = PublicKey(self.n, self.e)
		else :
			pass


	#Return the PKCS#1 RSA encryption of "text" as an even-length hex string
	def Encrypt(self, text):
		if text == None:
			return None
		ciphertext = encrypt(text,self.pubkey)
		return ''.join([("%x"% ord(x)).zfill(2) for x in ciphertext])

