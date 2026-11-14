#Fibonacci sequence using recursion
def fib(n):
  if n <= 1:
    return n
  return fib(n - 1) + fib(n - 2)

num=int(input("Enter a number: "))
for i in range(num+1):
  print(fib(i), end=" ")
