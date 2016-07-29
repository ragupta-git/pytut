#!/usr/bin/python

from string import join
from array import array
import sha
from time import time
from string import translate

class CryptError(Exception): pass
def _hash(str): return sha.new(str).digest()
#def _hash(str): return hmac.new("key", str, hashlib.sha256).hexdigest()
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
        seed=sha.new(key+seed).digest()
        #seed=hmac.new("key", key+seed, hashlib.sha256).hexdigest()
        xkey.append(seed)
    j = join(xkey,'')
    return array ('L', j)

def p3_encrypt(plain,key):
    print "\nInside Encrypt..."
    global _state
    H = _hash
    _state = 'X'+_state
    nlist = [`time()`, _pid, _state, `len(plain)`,plain, key]
    print nlist
    print join(nlist,',')
    print _ivlen
    print H(join(nlist,','))
    nonce = H(join(nlist,','))[:_ivlen]
    print "++++++++++"
    print nonce
    _state = H('update2'+_state+nonce)
    k_enc, k_auth = H('enc'+key+nonce), H('auth'+key+nonce)
    n=len(plain)                        # cipher size not counting IV

    stream = array('L', plain+'0000'[n&3:]) # pad to fill 32-bit words
    xkey = _expand_key(k_enc, n+4)
    for i in xrange(len(stream)):
        stream[i] = stream[i] ^ xkey[i]
    ct = nonce + stream.tostring()[:n]
    auth = _hmac(ct, k_auth)
    return ct + auth[:_maclen]

def p3_decrypt(cipher,key):
    print "\nInside Decrypt..."
    H = _hash
    n=len(cipher)-_ivlen-_maclen        # length of ciphertext
    if n < 0:
        raise CryptError, "invalid ciphertext"
    nonce,stream,auth = \
      cipher[:_ivlen], cipher[_ivlen:-_maclen]+'0000'[n&3:],cipher[-_maclen:]
    print nonce
    print stream
    print auth
    k_enc, k_auth = H('enc'+key+nonce), H('auth'+key+nonce)
    vauth = _hmac (cipher[:-_maclen], k_auth)[:_maclen]
    if auth != vauth:
        raise CryptError, "invalid key or ciphertext"

    stream = array('L', stream)
    xkey = _expand_key (k_enc, n+4)
    for i in xrange (len(stream)):
        stream[i] = stream[i] ^ xkey[i]
    plain = stream.tostring()[:n]
    return plain

def _hmac_setup():
    global _ipad, _opad, _itrans, _otrans
    _itrans = array('B',[0]*256)
    _otrans = array('B',[0]*256)    
    for i in xrange(256):
        _itrans[i] = i ^ 0x36
        _otrans[i] = i ^ 0x5c
    _itrans = _itrans.tostring()
    _otrans = _otrans.tostring()

    _ipad = '\x36'*64
    _opad = '\x5c'*64

def _hmac(msg, key):
    if len(key)>64:
        key=sha.new(key).digest()
    ki = (translate(key,_itrans)+_ipad)[:64] # inner
    ko = (translate(key,_otrans)+_opad)[:64] # outer
    return sha.new(ko+sha.new(ki+msg).digest()).digest()

_hmac_setup()


estr = p3_encrypt("Rahul","abc")
dstr = p3_decrypt(estr,"abc")
print "\n___MAIN___"
print estr
print dstr
