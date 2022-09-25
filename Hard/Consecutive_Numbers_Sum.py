class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        k=1
        c=0
        while k*(k-1)//2<n:
            if (n-(k*(k+1))//2)%k==0:
                c+=1
            k+=1
        return c
        