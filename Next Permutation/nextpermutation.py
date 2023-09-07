def nextGreaterPermutation(A):
    n=len(A)
    x=len(A)-1
    res=[]
    while x>0 and A[x]<=A[x-1]:
        x-=1
    if(x==0):
        return A.reverse()
    element_change=x-1
    #print(f"element change: {element_change} and position: {x}")
    A[x:]=reversed(A[x:]) 
    #print(A)
    while x<n and A[element_change]>A[x]:
        x+=1
    A[element_change],A[x]=A[x],A[element_change]
    return A
   
# A=[11,7,13,8,16,13]
B=[]
with open("D:\\Big Data\\Learn Python\\DSA\\Next Permutation\\input.txt") as f:
    B=f.read()
# print(B)
B=B.split()
B=[int(i) for i in B]
print(nextGreaterPermutation(B))