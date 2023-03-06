def fibonacci(n):
 
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    else:
        fib = [0, 1]
        while len(fib) <= n:
            fib.append(fib[-1] + fib[-2])
        
        if n in fib:
            return fib, f"O número {n} pertence à sequência de Fibonacci"
        else:
            return fib, f"O número {n} não pertence à sequência de Fibonacci"
        

fibonacci_sequence, mensagem = fibonacci(21)
print(fibonacci_sequence)
print(mensagem)