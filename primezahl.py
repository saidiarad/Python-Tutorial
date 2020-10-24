
def ist_prime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
    return prime

prime_count = 0
last_prime_zahl = 0
for i in range(1,100001):
    if ist_prime(i):
        last_prime_zahl = i
        prime_count = prime_count + 1

print ("")
print ("wir haben", prime_count, "primezahl")
print ("letze primezahl", last_prime_zahl)