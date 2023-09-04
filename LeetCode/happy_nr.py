class Solution:
    def isHappy(self, n):
        l =[]
        while n>10:
            l.append((n % 10)**2)
            n = n//10
        l.append(n**2)

        happy_sum = 0
        print(l)
        for i in range(len(l)):
            l[i] = l[i]*l[i]
            happy_sum = happy_sum + l[i]
        print(l)
        return True if happy_sum == 1 else False
        

s = Solution()
result = s.isHappy(19)
print(result)