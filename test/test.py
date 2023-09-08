def crivo_eratostenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
                
    prime_numbers = [p for p in range(2, n+1) if is_prime[p]]
    return prime_numbers

n = 50  # Altere o valor de 'n' conforme necessário
primes = crivo_eratostenes(n)
print(f"Números primos até {n}: {primes}")
