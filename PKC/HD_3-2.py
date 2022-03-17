from Crypto.Util.number import getPrime #only used for generating big primes for keys
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os import urandom

#Task 3 Part 2

def gcd(a, b):
   while a != 0:
      a, b = b % a, a
   return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def encode(msg, public_key):
    nummsg = int(msg.encode('utf-8').hex(), 16)
    return pow(nummsg, public_key[0], public_key[1])


def decode(encmsg, private_key):
    nummsg = pow(encmsg, private_key[0], private_key[1])
    return ascii(nummsg.to_bytes((nummsg.bit_length() + 7) // 8, byteorder='big'))

#Demonstrates a malleability attack
def main(): 
    p= getPrime(100)
    q= getPrime(100)
    n= p*q
    e = 65537
    public_key = (e, n)
    print("Alice created public key= " + str(public_key))
    print("Bob computes encryption for 'Hello Alice...'")
    c = encode("Hello Alice!", public_key)
    print("c = " + str(c))
    print("Mallory intercepts c and applies F(c) -------")
    c_alt = pow(c, public_key[0], public_key[1])
    print("new c= " + str(c_alt))
    print("Alice recieves the altered c and forms her new message 'Hi Bob!'")
    d = findModInverse(e, (p-1) * (q-1))
    private_key = (d, n)
    s = decode(c_alt, private_key)
    cipher = SHA256.new()
    cipher.update(bytes(str(s), encoding= "UTF-8"))
    k = cipher.digest()
    m = "Hi Bob!"
    iv = urandom(16)
    enc = AES.new(k, AES.MODE_CBC, iv)
    c0 = enc.encrypt(pad(bytes(m, encoding="utf-8"), 128))
    print("Alice sends out c0....")

    print("Mallory runs her own decryption on c0 using the known c_alt value...")
    dec = AES.new(k, AES.MODE_CBC, iv)
    cracked = unpad(dec.decrypt(c0), 128)
    print("Mallory recieves: " + str(cracked))

if __name__ == "__main__":
    main()