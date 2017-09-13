#program to remov the duplicates [1,2,4,5,1,3,6]

def remDuplicate(list):
#list=[1,2,4,5,1,3,6]
#print (list.count())
 s=[]
 for i in list:
    if i not in s:
      s.append(i)
 return s


item=[1,2,4,5,1,3,6]
s=remDuplicate(item)
print (s)
item1=['a','a','b','b','c','c']
y=remDuplicate(item1)
print(y)
