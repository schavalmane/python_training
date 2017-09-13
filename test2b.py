#program to return common items in two lists

def returnCommon(list1,list2):
#list=[1,2,4,5,1,3,6]
#print (list.count())
 s=[]
 for i in list1:
    if i in list2 and i not in s:
      s.append(i)
 return s


item1=[1,2,4,5,1,3,6]
item2=[1,2,3,1,2,3,4]
s=returnCommon(item1,item2)
print (s)
