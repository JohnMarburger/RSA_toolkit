##generate SSH key 
from Crypto.PublicKey import RSA
from os import chmod
##using https://stackoverflow.com/questions/2466401/how-to-generate-ssh-key-pairs-with-python
##as a guide, with slight modifications
def create():
    print("enter your desired key size")
    print("recomended key size is at least 4096")   
    size = int(input())
    keys = RSA.generate(size)
    print()
    private = input("enter the location and name you want the private key saved to")
    print()
    public = input(["enter the location and name you want the public key saved to"])
    ##remember to come back later and check its a valid location
    with open(private, 'wb') as content_file:
        content_file.write(keys.exportKey('PEM'))
    keys = keys.publickey()
    with open(public, 'wb') as content_file:
        content_file.write(keys.exportKey('PEM'))
