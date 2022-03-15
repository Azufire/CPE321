from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os import urandom

def main(): 
    p = 0xB10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371
    g = 0xA4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5

    #print("Given inital values: p=" + str(p) + " | g=" + str(g))

    #create public key and combine with private keys
    a = 1111
    b = 2222
    print("a=" + str(a) + " | b=" + str(b))
    x = pow(g, a) % p
    y = pow(g, b) % p

    a2 = pow(y,a) % p
    b2 = pow(x, b) % p

    #print("encrypted keys (should be equal): " + str(a2) + ", " + str(b2)) 
    assert a2 == b2

    #create hash k and use on keys
    k = SHA256.new()
    k.update(bytes(str(a2), encoding = "utf-8"))
    a2_hashed = k.digest()
    k.update(bytes(str(b2), encoding = "utf-8"))
    b2_hashed = k.digest()

    #truncate values to 16 bytes
    a2_hashed = a2_hashed[:16]
    b2_hashed = b2_hashed[:16]

    #encrypt messages (stonks)
    m0 = "Hi Bob!"
    m1 = "Hi Alice!"

    iv = urandom(16)
    enc0 = AES.new(a2_hashed, AES.MODE_CBC, iv)
    enc1 = AES.new(b2_hashed, AES.MODE_CBC, iv)

    c0 = enc0.encrypt(pad(bytes(m0, encoding="utf-8"), 128))
    c1 = enc1.encrypt(pad(bytes(m1, encoding="utf-8"), 128))

    #Decrypting the recieved messages
    dec0 = AES.new(a2_hashed, AES.MODE_CBC, iv)
    alice_text = unpad(dec0.decrypt(c0), 128)
    print("Alice recieved: " + str(alice_text))

    dec1 = AES.new(b2_hashed, AES.MODE_CBC, iv)
    bob_text = unpad(dec1.decrypt(c1), 128)
    print("Bob recieved: " + str(bob_text))







if __name__ == "__main__":
    main()