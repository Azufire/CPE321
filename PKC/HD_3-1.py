from Crypto.Util.number import getPrime #only used for generating big primes for keys
import sys
import binascii

#Task 3 Part 1

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

#heavy lifting code with many back problems
def generateKeys(keylen):
    p= getPrime(keylen) #max 1024
    q= getPrime(keylen)
    n= p*q
    e = 65537

    #calculate private key
    d = findModInverse(e, (p-1) * (q-1))
    public_key = (e, n)
    private_key = (d, n)
    print("Created public key= " + str(public_key))
    print("Created private key= " + str(private_key))
    return (public_key, private_key)

def encode(msg, public_key):
    nummsg = int(msg.encode('utf-8').hex(), 16)
    return pow(nummsg, public_key[0], public_key[1])


def decode(encmsg, private_key):
    nummsg = pow(encmsg, private_key[0], private_key[1])
    return ascii(nummsg.to_bytes((nummsg.bit_length() + 7) // 8, byteorder='big'))

def main(): 
    if len(sys.argv) != 4:
        print("usage: python HD_3-1.py [encode|both] [key length] [msg]")
    else:
        public_key, private_key = generateKeys(int(sys.argv[2]))
        print("Keys created")
        if sys.argv[1] == "encode":
            results = encode(sys.argv[3], public_key)
            print(results)
        elif sys.argv[1] == "both":
            print("Encoded:")
            results= encode(sys.argv[3], public_key)
            print(results)
            print("Decoded:")
            print(decode(results, private_key))
        else:
            print("usage: python HD_3-1.py [encode}decode|both] [msg]")

if __name__ == "__main__":
    main()