#pyjsbn-rsa
Python RSA module compatible with [jsbn.js](https://github.com/jasondavies/jsbn).


##Installation

pyjsbn-rsa is available via PyPI

    pip install pyjsbn-rsa

via setup.py

	python setup.py install
	
##Basic Use
You can test module with [jsbn's RSA Encryption Demo](http://www-cs-students.stanford.edu/~tjw/jsbn/rsa.html)

    >>from jsbn import RSAKey
    >>rsa = RSAKey()
    >>rsa.Generate(1024,"10001")
    >>hex(rsa.n)
    0xdc36096d038a56e84c6290f33db80dce54413e89dc15f0490dde8f1f58e69d957eed66c9537918b8fefd6a3fc9fc7b2551ac595bc77c2b98bcfa13f7deb17e94890ae4f28016f0d3e09450054263ae71f81539b09ea42b854492691e94de5671835b4ce91b9756b651ec4bbebe63eec8b7274e157b8de07457f2d3563119ac53L

    
Paste rsa.n to demo's *Modulus (hex)* and press encryt. (without "0x" and "L") And, get *Ciphertext (hex)* value

    >>ctext="ceffa610eb7ec7fcbda60b2fdecf6d7cc65b7304ecb6e327056f15d763f1d079d376dbc801861a0ccb2731f836e75de0bb22350b3cd0d18eed216619b9e64a59dc06e15ef2531f0d3c176882444c5919dd751e9bcaefadff372d847b001a298751ebc69f9d310d92c217ab2fa433e3b3c7e8edf4744849560a317ef7f4ee7266"
    >>rsa.Decrypt(ctext)
    'Hello World!'
    

##Methods
You can use man methods of rsa.js and rsa2.js

###SetPublic
Set the public key fields N and e from hex strings
    >>rsa.SetPublic(n,e)

###SetPrivate
Set the private key fields N, e, and d from hex strings
	>>rsa.SetPrivate(n,e,d)