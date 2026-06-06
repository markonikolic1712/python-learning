def is_prime(n):
    if n == 1: return False
    prime_num = True
    i = 2
    while i <= n:
        if n % i == 0 and i != n:
            prime_num = False
        i += 1

    return prime_num

print(f"is_prime(1): {is_prime(1)}")
print(f"is_prime(2): {is_prime(2)}") # prime
print(f"is_prime(3): {is_prime(3)}") # prime
print(f"is_prime(4): {is_prime(4)}")
print(f"is_prime(5): {is_prime(5)}") # prime
print(f"is_prime(6): {is_prime(6)}")
print(f"is_prime(7): {is_prime(7)}") # prime
print(f"is_prime(11): {is_prime(11)}") # prime
print(f"is_prime(59): {is_prime(59)}") # prime
print(f"is_prime(60): {is_prime(60)}")
print(f"is_prime(61): {is_prime(61)}") # prime
print(f"is_prime(62): {is_prime(62)}")


