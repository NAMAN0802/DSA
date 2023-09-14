class Solution:
    def sortColors(self, nums) -> None:
        n=len(nums)
        low=mid=0
        high=n-1
        while mid<=high:
            if(nums[mid]==0):
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1

if __name__=="__main__":  
    s=Solution()
    B=[]
    with open("D:\\Big Data\\Learn Python\\DSA\\Sort 0's, 1's and 2's\\input.txt") as st:
        B=st.read()
    B=B.split()
    B=[int(i) for i in B]
    s.sortColors(B)
    print(B)

