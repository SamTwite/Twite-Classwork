### SRC - I think there is more code to go in here
### you need to compare timings with the iterative version.

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2) 
    #endif
#endfunction
fib(5)
