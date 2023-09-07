from math import *

'''if empty subarray supported []'''
def maxSubarraySum(arr) :
    ans=-inf
    temp=0
    for i in arr:
        temp+=i
        if temp<0:
            temp=0
        ans=max(ans,temp)
    return ans

'''if empty subarray not supported. Means there should be a element present in the subarray'''
def maxSubArray(arr):
        ans=-inf
        temp=0
        for i in arr:
            temp+=i
            ans=max(ans,temp)
            if temp<0:
                temp=0
        return ans

if __name__=="__main__":
    arr=[]
    with open("D:\\Big Data\\Learn Python\\DSA\\Maximum sum subarray (Kadans Algo)\\input.txt") as f:
        arr=f.read();
    arr=arr.split();
    arr=[int(i) for i in arr]
    print(arr)
    print(f"if empty array not supported: {maxSubArray(arr)}")
    print(f"if empty array supperted: {maxSubarraySum(arr)}")