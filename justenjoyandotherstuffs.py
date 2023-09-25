class Dsa:
    def factorial(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            return self.factorial(n-1) * n
        

answer = Dsa()
result = answer.factorial(5)
print(result)

class DSA2:
    def fibonacci(self, n: int) -> int:
        if (n == 1):
            return 1
        elif(n == 0):
            return 0
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
        
answer = DSA2()

result = answer.fibonacci(7)
print(result)
