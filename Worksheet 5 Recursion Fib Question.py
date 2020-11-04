def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2) 
    #endif
#endfunction
print(fib(40))
def fibonacci2(n)
    fibNumbers = [0,1]  #list of first two Fibonacci numbers
	# now append the sum of the two previous numbers to the list    
    for i = 2 to n
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
	next i
	return fibNumbers[n] 
#endfunction


