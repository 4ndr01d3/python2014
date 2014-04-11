f = open("file.txt","r+")
print f.tell()
f.seek(30,2)
f.write("X")
print f.tell()
f.seek(-3,2)
print f.tell()
for any in f:
    print any,
f2 = open("newfile.txt","w")
for i in range(100):
    if i%2==0:
        f2.write("*"*i + "\n")
    else:
        f2.write("-"*i + "\n")
f2.close()