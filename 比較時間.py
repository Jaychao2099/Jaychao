import time

print("求a ^ N mod m = ? (其中 N 極大)")
aa = int(input("請輸入 a: "))
NN = int(input("請輸入 N: "))
mm = int(input("請輸入 m: "))

start_time1 = time.time()

######################################################################

def mod_exp(a, N, m):
    x = 1
    power = a % m
    while N > 0:
        if N % 2 == 1:
            x = (x * power) % m
        power = (power**2) % m
        N = N //2
    return x

print(f"{aa} ^ {NN} mod {mm} = {mod_exp(aa, NN, mm)}")

######################################################################

end_time1 = time.time()

######################################################################

def mod_exp_d(a, N, m):
    x = (a ** N) % m
    return x

print(f"{aa} ^ {NN} mod {mm} = {mod_exp(aa, NN, mm)}")

######################################################################

end_time2 = time.time()

######################################################################

execution_time1 = end_time1 - start_time1
execution_time2 = end_time2 - end_time1

print(f"Program_1 運算時間 = {execution_time1} s")
print(f"Program_2 運算時間 = {execution_time2} s")

if execution_time1 < execution_time2:
    print(f"Program_1 運算時間 < Program_2 運算時間.")
elif execution_time1 > execution_time2:
    print(f"Program_1 運算時間 > Program_2 運算時間.")
else:
    print(f"Program_1 運算時間 = Program_2 運算時間.")