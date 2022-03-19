from nltk.corpus import words
import bcrypt
import time
import sys

def find_salt(data):
    data = data.split(":")[1]
    return data[:29]


def decrypt(codeList):
    crackedCodes = 0
    numCodes = len(codeList)
    salt = find_salt(codeList[0])
    encodeList = [c.split(":")[1].encode() for c in codeList]
    wordsList = words.words()
    startTime = time.time()

    for word in wordsList:
        if len(word) >= 6 and len(word) <= 10:   
            hashval = bcrypt.hashpw(word.encode("utf-8"), salt.encode("utf-8"))
            for x in range(len(encodeList)):
                if hashval == encodeList[x]:
                    name = (codeList[x]).split(":")[0]
                    currentTime = time.time() - startTime
                    print(name + " password= " + word + " at t= " + str(currentTime))

                    crackedCodes += 1
                    if crackedCodes == numCodes:
                        print("done")
                        return



def main():
    if len(sys.argv) < 2:
        print("usage: Task2.py [8-13]")
    elif sys.argv[1] == "8":
        print("Hashing 8 costs:")
        codeList = []
        codeList.append("Bilbo:$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq")
        codeList.append("Gandalf:$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC")
        codeList.append("Thorin:$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q")
        decrypt(codeList)

    elif sys.argv[1] == "9":
        print("Hashing 9 costs:")
        codeList = []
        codeList.append("Fili:$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm")
        codeList.append("Kili:$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im")
        decrypt(codeList)

    elif sys.argv[1] == "10":
        print("Hashing 10 costs:")
        codeList = []
        codeList.append("Balin:$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom")
        codeList.append("Dwalin:$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be")
        codeList.append("Oin:$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK")
        decrypt(codeList)

    elif sys.argv[1] == "11":
        print("Hashing 11 costs:")
        codeList = []
        codeList.append("Gloin:$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q")
        codeList.append("Dori:$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq")
        codeList.append("Nori:$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12")
        decrypt(codeList)

    elif sys.argv[1] == "12":
        print("Hashing 12 costs:")
        codeList = []
        codeList.append("Ori:$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O")
        codeList.append("Bifur:$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK")
        codeList.append("Bofur:$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O")
        decrypt(codeList)

    elif sys.argv[1] == "13":
        print("Hashing 13 costs:")
        codeList = []
        codeList.append("Durin:$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay")
        decrypt(codeList)

    else:
        print("usage: Task2.py [8-13]")


if __name__ == "__main__":
    main()