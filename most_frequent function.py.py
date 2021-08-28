def most_frequent(a):
    d={}
    for i in a:
        b=a.count(i)
        d[i]=b
    return d
string=input("Please enter a string: ")
f=most_frequent(string)
sf=sorted(f.items(),key=lambda x:x[1],reverse=True)
for i in sf:
    print("%s = %02d"%(i[0],i[1]))
            
    
