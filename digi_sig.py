from random import *
from hashlib import sha1

from Crypto.Util.number import *


class DigitalSignature:
  ### Implementation of Digital Signature for IS IA-1
  ### Submission by Roll no. 84,85,91,92

  # Global parameters are q,p, and g
  def param_gen(self):
    # primes of 8 bits in length in binary
    # q is prime divisor
    q = getPrime(5)
    # p is prime modulus
    p = getPrime(10)

    # Always p should be greater than q because p-1 must be a multiple of q
    # to make sure that p not equal to q while generating randomly and q is prime divisor of p-1
    while ((p - 1) % q != 0):
      p = getPrime(10)
      q = getPrime(5)

    print("Prime divisor (q): ", q)
    print("Prime modulus (p): ", p)

    flag = True
    while (flag):
      h = int(input("Enter integer between 1 and p-1(h): "))
      # h must be in between 1 and p-1
      if (1 < h < (p - 1)):
        g = 1
        while (g == 1):
          g = pow(h, int((p - 1) / q)) % p
        flag = False
      else:
        print("Wrong entry")
    print("Value of g is : ", g)

    # returning them as they are public globally
    return (p, q, g)

  def keygen(self, p, q, g):
    # User private key:
    x = randint(1, q - 1)
    print("Randomly chosen x(Private key) is: ", x)

    # User public key:
    y = pow(g, x) % p
    print("Randomly chosen y(Public key) is: ", y)

    # returning private and public components
    return (x, y)

  # Hash of message in SHA1
  def hash_function(self, message):
    hashed = sha1(message.encode("UTF-8")).hexdigest()
    return hashed

  # Modular Multiplicative Inverse
  def inverse(self, a, m):
    a = a % m
    for x in range(1, m):
      if ((a * x) % m == 1):
        return (x)
    return (1)

  def sign(self, name, p, q, g, x):
    with open(name) as file:
      text = file.read()
      hash_component = self.hash_function(text)
      print("Hash of document sent is: ", hash_component)
    r = 0
    s = 0
    while (s == 0 or r == 0):
      k = randint(1, q - 1)
      r = ((pow(g, k)) % p) % q
      i = self.inverse(k, q)

      # converting hexa decimal to binary
      hashed = int(hash_component, 16)
      s = (i * (hashed + (x * r))) % q

    # returning the signature components
    return (r, s, k)

  def verify(self, name, p, q, g, r, s, y):
    with open(name) as file:
      text = file.read()
      hash_component = self.hash_function(text)
      print("Hash of document received is: ", hash_component)

    # computing w
    w = self.inverse(s, q)
    print("Value of w is : ", w)

    hashed = int(hash_component, 16)

    # computing u1, u2 and v
    u1 = (hashed * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1) * pow(y, u2)) % p) % q

    print("Value of u1 is: ", u1)
    print("Value of u2 is: ", u2)
    print("Value of v is : ", v)

    if (v == r):
      print("The signature is valid!")
    else:
      print("The signature is invalid!")


def main():
  ds = DigitalSignature()
  var = ds.param_gen()
  keys = ds.keygen(var[0], var[1], var[2])

  # Sender's side (signing the document):
  print()
  file_name = input("Enter name of document to sign: ")
  components = ds.sign(file_name, var[0], var[1], var[2], keys[0])

  print("r(Component of signature) is: ", components[0])
  print("k(Randomly chosen number) is: ", components[2])
  print("s(Component of signature) is: ", components[1])

  # Receiver's side (verifying the sign):
  print()
  file_name = input("Enter the name of document to verify: ")
  ds.verify(file_name, var[0], var[1], var[2], components[0], components[1],
            keys[1])


if __name__ == '__main__':
  main()
