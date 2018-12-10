from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

from runstats import Statistics
from decimal import Decimal
#from Crypto import Random
import os
import random
import base64
from pkcs7 import PKCS7Encoder

# Using AES_BLOCK_SIZE = 16 , can be a multiple of 16


class NsuCryptoServer:
      def __init__(self):
            try:
                  self.encoder = PKCS7Encoder()
                  self.runningStat = Statistics()
                  self.rAvg = 0.0
                  self.rDev = 0.0
                  if "AES_KEY" in os.environ:
                        self.skey = os.environ["AES_KEY"]
                  else:
                        self.skey = os.urandom(16)
                  self.iv = ''.join([chr(random.randint(0, 0xFF))
                                     for i in range(16)])
            except Exception as e:
                  print "Failed to Initialize NsuCryptoServer:"+str(e)

      def encrypt(self, PlainText):
            cipher = AES.new(self.skey, AES.MODE_CBC, self.iv)
            padded_data = self.encoder.encode(PlainText)
            return base64.b64encode(cipher.encrypt(padded_data))

      def decrypt(self, CipherText):
            cipher = AES.new(self.skey, AES.MODE_CBC, self.iv)
            decrypted_data = cipher.decrypt(base64.b64decode(CipherText))
            return self.encoder.decode(decrypted_data)

      def calculateStat(self, input, encryptflag):
            self.runningStat.push(input)
            rMean = self.runningStat.mean()
            if len(self.runningStat) == 1:
                  rDeviance = 0
            else:
                  rDeviance = self.runningStat.stddev(ddof=0) # Setting Degrees of Freedom to 0 contrast to the default 1 based on requirement
            if encryptflag == True:
                  return "{"+self.encrypt(str(rMean))+","+self.encrypt(str(rDeviance))+"}"
            else:
                  return "{"+str(rMean)+","+str(rDeviance)+"}"

      def reset(self):
            try:
                  self.runningStat.clear()
            except Exception as e:
                  return "Failure:"+str(e)
