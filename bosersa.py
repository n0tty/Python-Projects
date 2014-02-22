#!/usr/bin/python


#Greetz
def greet():
  print \
  """
  RSA implementation by n0tty\n
  legendtanoybose@gmail.com
  http://the-bose.com
  
__________                     
\\______   \\ ____  ______ ____  
 |    |  _//  _ \\/  ___// __ \\ 
 |    |   (  <_> )___ \\\\  ___/ 
 |______  /\\____/____  >\\___  >
        \\/           \\/     \\/ 
  """


greet()


#Module start

import random
from itertools import combinations
import math
import copy
 
 
def euclid(a, b):
  '''returns the Greatest Common Divisor of a and b'''
  a = abs(a)
  b = abs(b)
  if a < b:
    a, b = b, a
  while b != 0:
    a, b = b, a % b
  return a
 
 
def coprime(l):
  '''returns 'True' if the values in the list L are all co-prime
  otherwier, it returns 'False'. '''
  for i, j in combinations(l, 2):
    if euclid(i, j) != 1:
      return False
  return True
 
def extendedEuclid(a, b):
    '''return a tuple of three values: x, y and z, such that x is
    the GCD of a and b, and x = y * a + z * b'''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extendedEuclid(b % a, a)
        return (g, x - (b // a) * y, y)
 
 
def modInv(a, m):
    '''returns the multiplicative inverse of a in modulo m as a
       positve value between zero and m-1'''
    # notice that a and m need to co-prime to each other.
    if coprime([a, m]) == False:
        return 0
    else:
        linearcombination = extendedEuclid(a, m)
        return linearcombination[1] % m
 

def get_mod():
        '''Asks for 2 prime numbers p & q and calculates the public and private keys'''
        print 'Enter the two Prime Numbers p & q: '
        p = input()
        q = input()
        n = p*q
        t = (p-1)*(q-1)
        while True:
                e = random.randint(2,(t-1))
                if coprime([e, t]):
                        break
        d = modInv(e, t)
        if (d==0 & e==d):
                get_mod(p,q)
        print e,d
        return n,e,d


#encryption
def encrypt(a,e,n):
    '''Takes message, pubkey, modulo as input and gives encrypted message output'''
    print 'Entered Message: ',a
    b = [ord(c) for c in a]
    print 'Encrypting with Public Key:',e,',',n
    crypt = []
    for i in b:
        j = pow(i,e,n)
        crypt.append(j)

    return crypt

#decryption
def decrypt(crypt,d,n):
    '''Takes ciphertex,pvtkey and modulo and decrypts and retrives original message'''
    print 'Entered Ciphertext: ',crypt
    print 'Decrypting with Private Key:',d,',',n
    fin = []
    for k in crypt:
        l = pow(k,d,n)
        fin.append(l)

    final_msg = [chr(h) for h in fin]
    dec_msg = ''.join(final_msg)

    return dec_msg

