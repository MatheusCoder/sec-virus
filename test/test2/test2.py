def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        result = 1
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result

n = 10  # Altere o valor de 'n' para obter diferentes termos da sequência Fibonacci
fibonacci_sequence = [fibonacci(i) for i in range(1, n + 1)]
print(f"Sequência de Fibonacci até o {n}-ésimo termo: {fibonacci_sequence}")
