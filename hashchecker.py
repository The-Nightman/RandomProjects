import hashlib#importing hash library

hashcryp = hashlib.md5()#this ties the MD5 haslib as the hashcryp variable
hashcryp2 = hashlib.md5()#this ties the MD5 haslib as the hashcryp2 variable for the second file

with open('dog.jpg', 'rb') as file1:#enter file name and extension to read the file, file is read as binary for MD5 to work
    file1hash = file1.read()
    hashcryp.update(file1hash)
hash1 = hashcryp.hexdigest()
print(hashcryp.hexdigest())

with open('dog altered.jpg', 'rb') as file2:#enter file name and extension to read the file, file is read as binary for MD5 to work
    file2hash = file2.read()
    hashcryp2.update(file2hash)
hash2 = hashcryp2.hexdigest()
print(hashcryp2.hexdigest())

if hash1 == hash2:#if statement checks the value of the hash variables and prints an output accordingly
    print("MD5 hash signature match")
else:
    print("MD5 hash signatures do not match, please check that the correct files are entered otherwise the file may have been altered")