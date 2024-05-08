import time

num1 = int(input("base = "))
num2 = int(input("exp = "))

start_time1 = time.time()

######################################################################

def power_re(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_re(a * a, n // 2)
    else:
        return power_re(a, n-1) * a

ppp_re = power_re(num1, num2)
# print(f"{num1}^{num2} = {ppp_re}")

######################################################################

end_time1 = time.time()

start_time2 = time.time()

######################################################################

def power_lo(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a
        a *= a
        n //= 2
    return result

ppp_lo = power_lo(num1, num2)
# print(f"{num1}^{num2} = {ppp_lo}")

######################################################################

end_time2 = time.time()

######################################################################

execution_time1 = end_time1 - start_time1
execution_time2 = end_time2 - start_time2

print(f"Program_re 運算時間 = {execution_time1} s")
print(f"Program_lo 運算時間 = {execution_time2} s")

if execution_time1 < execution_time2:
    print(f"Program_re 運算時間 < Program_lo 運算時間.")
elif execution_time1 > execution_time2:
    print(f"Program_re 運算時間 > Program_lo 運算時間.")
else:
    print(f"Program_lo 運算時間 = Program_re 運算時間.")