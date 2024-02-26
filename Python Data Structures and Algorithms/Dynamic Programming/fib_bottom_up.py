def fib(n):
    fib_list = [0,1]
    
    for index in range(2, n + 1):
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
        
    return fib_list[n]
        