import time

used_time=time.time()

top=100000

is_prime=[True]*(top+1)

is_prime[0]=is_prime[1]=False

for num in range(2, int(top ** 0.5)+1):
    if is_prime[num]:
        for multiple in range(num * num, (top+1), num):
            is_prime[multiple]=False

primes = [i for i, val in enumerate(is_prime) if val]

used_time = time.time() - used_time

print("Between 1-",top+1,"all primes are:")
print(primes)
print("Totally used:", used_time, " seconds.")



