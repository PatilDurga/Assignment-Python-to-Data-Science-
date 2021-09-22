def eve_num(li):
    """Return the Even numbers from the List
    >>> eve_num([1,4,5,99,124])
    4
    124
    """
    result=[]
    n=len(li)
    for i in range(0,n):
        if(li[i]%2==0):
            result.append(li[i])
          
    return result
li=[2,5,6,8,7,3,88,124,99]
ans=eve_num(li)
print("List :",li)
print("Even numbers:")
for i in range(0,len(ans)):
    print(ans[i])

