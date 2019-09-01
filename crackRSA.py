##tool for factoring
##https://crypto.stackexchange.com/questions/46695/how-to-factor-an-rsa256-public-key-with-yafu
##^ great basis for how I'm going to do things, credit goes to those in the thread
##"https://crypto.stackexchange.com/questions/46695/how-to-factor-an-rsa256-public-key-with-yafu""
from Crypto.PublicKey import RSA
#credit to https://crypto.stackexchange.com/users/11718/squeamish-ossifrage for this code(lines 7-34)
def egcd(a, b):
    """Extended Euclidean algorithm"""
    """https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm"""
    x,y,u,v = 0,1,1,0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b,a,x,y,u,v = a,r,u,v,m,n
    return b, x, y

def modinv(e, m):
    """Modular multiplicative inverse"""
    """https://en.wikipedia.org/wiki/Modular_multiplicative_inverse"""
    g, x, y = egcd(e, m) 
    if g != 1:
        return None
    else:
        return x % m

def pqe2rsa(p, q, e):
    """Generate an RSA private key from p, q and e"""
    from Crypto.PublicKey import RSA
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    key_params = (long(n), long(e), long(d), long(p), long(q))
    priv_key = RSA.construct(key_params)
    print(priv_key.exportKey())
##now from here on this is my code
def factor():
    print("Please paste the public key into a text file and save it as a .pub")
    results = RSA.importKey(open('key.pub', 'r').read()) ##read file in
    n = results.n
    e = results.e
    print("e = " + str(e) + " and n = " + str(n))
    print()
    print("factor the n value you just fot using YAFU or msieve")
    p = int(input("enter the p value"))
    q = int(input("enter the q value"))
    e = int(input("enter the e value"))
    pqe2rsa(p, q, e)
    print("we just generated a private key by factoring the public key")
factor()
