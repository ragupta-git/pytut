#!/usr/bin/python

from string import join
from array import array
import sha
from time import time
from string import translate
import hashlib
import hmac
import base64

class CryptError(Exception): pass
#def _hash(str): return sha.new(str).digest()
def _hash(str): return hashlib.sha256(str).hexdigest()

_ivlen = 16
_maclen = 8
_state = _hash(`time()`)


try:
    import os
    _pid = `os.getpid()`
except ImportError, AttributeError:
    _pid = ''

def _expand_key(key, clen):
    blocks = (clen+19)/20
    xkey=[]
    seed=key
    for i in xrange(blocks):
        #seed=sha.new(key+seed).digest()
        seed=hashlib.sha256(key+seed).hexdigest()
        xkey.append(seed)
    j = join(xkey,'')
    return array ('L', j)

def encrypt(plain,key):
    global _state
    H = _hash
    _state = 'X'+_state
    nlist = [`time()`, _pid, _state, `len(plain)`,plain, key]
    nonce = H(join(nlist,','))[:_ivlen]
    _state = H('update2'+_state+nonce)
    k_enc, k_auth = H('enc'+key+nonce), H('auth'+key+nonce)
    n=len(plain)                        # cipher size not counting IV

    stream = array('L', plain+'0000'[n&3:]) # pad to fill 32-bit words
    xkey = _expand_key(k_enc, n+4)
    for i in xrange(len(stream)):
        stream[i] = stream[i] ^ xkey[i]
    ct = nonce + stream.tostring()[:n]
    #auth = _hmac(ct, k_auth)
    auth = hmac.new(k_auth, ct, hashlib.sha256).hexdigest()
    encryptStr = ct + auth[:_maclen]
    encodedStr = base64.encodestring(encryptStr)
    finalStr = encodedStr.rstrip('\n')
    return finalStr

def decrypt(cipher,key):
    H = _hash
    cipher = cipher+"\n"
    cipher = base64.decodestring(cipher)
    n=len(cipher)-_ivlen-_maclen        # length of ciphertext
    if n < 0:
        raise CryptError, "invalid ciphertext"
    nonce,stream,auth = \
      cipher[:_ivlen], cipher[_ivlen:-_maclen]+'0000'[n&3:],cipher[-_maclen:]
    k_enc, k_auth = H('enc'+key+nonce), H('auth'+key+nonce)
    #vauth = _hmac (cipher[:-_maclen], k_auth)[:_maclen]
    vauth = hmac.new(k_auth, cipher[:-_maclen], hashlib.sha256).hexdigest()[:_maclen]
    if auth != vauth:
        raise CryptError, "invalid key or ciphertext"

    stream = array('L', stream)
    xkey = _expand_key (k_enc, n+4)
    for i in xrange (len(stream)):
        stream[i] = stream[i] ^ xkey[i]
    plain = stream.tostring()[:n]
    return plain


