"""
Test for RSA
"""

from jsbn import RSAKey
import unittest


class BasicTest(unittest.TestCase):
    def test_basic(self):
        rsa = RSAKey()
        rsa.generate(1024, "10001")
        msg = 'Hello World!'
        cmsg = rsa.encrypt(msg)
        self.assertEqual(rsa.decrypt(cmsg), msg)


if __name__ == '__main__':
    unittest.main()
