def nextGreaterPermutation(A):
    n=len(A)
    x=len(A)-1
    res=[]
    while x>0 and A[x]<=A[x-1]:
        x-=1
    if(x==0):
        return sorted(A)
    element_change=x-1
    #print(f"element change: {element_change} and position: {x}")
    res=A[:x]+sorted(A[x:])
    #print(A)
    while x<n and res[element_change]>res[x]:
        x+=1
    res[element_change],res[x]=res[x],res[element_change]
    return res
   
# A=[11,7,13,8,16,13]
B=[]
with open("input.txt") as f:
    B=f.read()
# print(B)
B=B.split()
B=[int(i) for i in B]
print(nextGreaterPermutation(B))