n = int(input(":"))
m = n-1
def fib(m):
    if m == 0 :
        return 0
    elif m ==1 :
        return 1
    else :
        return fib(m-1) + fib(m-2)
print(fib(m), end=" ")

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# # Calculate the first 10 Fibonacci numbers
# for i in range(10):
#     print(fibonacci(i), end=" ")
