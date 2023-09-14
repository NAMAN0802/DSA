class Solution:
    def maxProfit(self, prices) -> int:
        ans=0
        left=prices[0]
        right=prices[0]
        for i in prices:
            if(i<left):
                left=right=i
            if(i>right):
                right=i
                ans=max(ans,right-left)    
        return ans
    
if __name__=="__main__":  
    s=Solution()
    B=[]
    with open("D:\\Big Data\\Learn Python\\DSA\\Stock Buy and Sell\\input.txt") as st:
        B=st.read()
    B=B.split()
    B=[int(i) for i in B]
    ans=s.maxProfit(B)
    print(ans)
