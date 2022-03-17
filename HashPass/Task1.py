from Crypto.Hash import SHA256
import sys

#Modified part A code: hashes but cuts output to first 50 bits max
def badhash(input):
    hasher = SHA256.new()
    hasher.update(input.encode())
    return hasher.hexdigest()[:50]

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
    target = badhash("doggo")
    print("Given target string doggo's hash= " + badhash("doggo"))

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