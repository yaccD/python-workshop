import time

used_time = time.time()
top=100000

primes=[]

for num in range(2,top+1):
    is_prime=True

    #check if num is prime
    for i in range(2,num):
        if num % i == 0:
            #as long as num is not prime, check next number
            is_prime = False
            break
    #if num is prime, collect the nubmer in list primes
    if is_prime:
        primes.append(num)

used_time=time.time() - used_time
print("Between 1-", top, ", all primes are:")
print(primes)
print("totaly use:", used_time, " seconds.")


