import time

num1 = int(input("base = "))
num2 = int(input("exp = "))

start_time = time.time()

######################################################################

def power(a, n):
    if n == 0:
        return 1
    elif a % 2 == 0:
        return power(power(a, n/2), 2)
    else:
        return power(a, n-1) * a

ppp = power(num1, num2)
print(f"{num1}^{num2} = {ppp}")

######################################################################

end_time = time.time()
execution_time = end_time - start_time

print("運算時間: {:.20f} 秒".format(execution_time))
