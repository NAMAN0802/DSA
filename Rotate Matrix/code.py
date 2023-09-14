class Solution:
    def rotate(self, matrix) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        
if __name__=="__main__":  
    s=Solution()
    B=[]
    temp=True
    with open("D:\\Big Data\\Learn Python\\DSA\\Rotate Matrix\\input.txt") as st:
        while temp:
            temp=st.readline()
            temp=temp.split()
            temp=[int(i) for i in temp]
            B.append(temp)
    print(B[:-1])
    s.rotate(B[:-1])
    print(B[:-1])
    