s = "The quick brown fox jumps slowly over the lazy cow"
index=0
while index!=-1:
    index = s.find("l",index)
    if index != -1: #found it
        print index        
        index += 1


print "With FOR"
howmany = s.count("l")         
index=0
for i in range(howmany):
    index = s.find("l",index)
    if index != -1: #found it
        print index        
        index =index+1