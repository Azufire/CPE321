from Crypto.Hash import SHA256
from random import choice
import sys
import time
import string

#Uses SHA256 to hash arbitrary input and prints digests to screen
def sha_hash(input):
    hasher = SHA256.new()
    hasher.update(input.encode())
    print("Encoded SHA256 String of " + input  + ": "+ hasher.hexdigest())

#Hashes 2 strings whose Hamming distance is exactly 1 bit
def partB():
    print("Hashing strings aaa and aab:")
    sha_hash("aaa")
    sha_hash("aab")
    print("Hashing strings of rad and sad:")
    sha_hash("rad")
    sha_hash("sad")
    print("Hashing strings doggo and dogho:")
    sha_hash("doggo")
    sha_hash("dogho")

#Truncates digest to 8-50 bits, finds collision
def partC():
    print("Calculating collisions for range (8, 52, 2)")
    chars = string.ascii_letters + string.digits
    for digestSize in range(8, 52, 2):
        print("calculating digest size " + str(digestSize))
        hashList = {}
        input = 0
        #create binary string of hash, truncate to digestSize
        hasher = SHA256.new()

        startTime = time.time()
        found = False

        while not found:                                #loop through different input hashes
            #create hash of random string of proper size
            randomStr = ''.join(choice(chars) for i in range(digestSize))
            hasher.update((str)(randomStr).encode("utf-8"))
            currHash = hasher.hexdigest()
            currHash = str(bin(int(currHash, 16)))
            currHash = currHash[:digestSize]

            #if hash in hashList, mark collision and break
            if currHash in hashList.keys():
                print("With [" + str(input) + "] inputs, found collision [" + currHash + "]") 
                endTime = time.time() - startTime
                print("Time taken= " + str(endTime))
                found = True
                break
            #otherwise add to hashlist and increment input counter
            hashList[currHash] = input
            input += 1






def main():
    if len(sys.argv) < 2:
        print("usage: Task1.py [A/B/C] [input (optional)]")
    elif sys.argv[1] == "A":
        print("Running Part A:")
        sha_hash(sys.argv[2])
    elif sys.argv[1] == "B":
        print("Running Part B:")
        partB()
    elif sys.argv[1] == "C":
        print("Running Part C:")
        partC()
    else:
        print("usage: Task1.py [A/B/C] [input]")



if __name__ == "__main__":
    main()