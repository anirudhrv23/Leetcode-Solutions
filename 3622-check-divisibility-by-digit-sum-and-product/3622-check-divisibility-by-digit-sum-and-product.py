class Solution:
    def checkDivisibility(self, n: int) -> bool:

        n1=n
        dig_sum = 0
        dig_prod=1

        while n1>0:
            a = n1%10

            dig_sum+=a
            dig_prod*=a
            n1//=10
        
         
        return n%(dig_sum+dig_prod) == 0
        