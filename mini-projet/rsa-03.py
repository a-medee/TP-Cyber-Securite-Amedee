import random

def power(a, b, m):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

def euclide_etendu(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclide_etendu(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def inverse(e, phi):
    gcd, x, y = euclide_etendu(e, phi)
    if gcd != 1: raise ValueError("Pas d'inverse")
    return x % phi

def is_prime_miller_rabin(n, k=5):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_small_prime(bits=16):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1
        if is_prime_miller_rabin(num):
            return num

p = generate_small_prime(16)
q = generate_small_prime(16)

while p == q: q = generate_small_prime(16)
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = inverse(e, phi)

print(f"Clés générées : Public=(e={e}, n={n}), Privé=(d={d}, n={n})")

message = 12345
print(f"Message clair : {message}")

cipher = power(message, e, n)
print(f"Chiffré : {cipher}")

plain = power(cipher, d, n)
print(f"Déchiffré : {plain}")
