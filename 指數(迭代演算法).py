import time
## import sys

num1 = int(input("base = "))
num2 = int(input("exp = "))

start_time = time.time()

######################################################################

def power(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a
        a *= a
        n //= 2
    return result

ppp = power(num1, num2)
print(f"{num1}^{num2} = {ppp}")

######################################################################

end_time = time.time()
execution_time = end_time - start_time

print("運算時間: {:.100f} 秒".format(execution_time))
# sys.set_int_max_str_digits(1000000)