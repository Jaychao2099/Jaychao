def fff(x, a1,a2,a3, p1,p2, ex1,exp, f0, f1, f2):
    n = 3
    while n <= x:
        result = a1*f2 + a2*f1 + a3*f0 + p1*n + p2 + ex1*exp**n
        if n <= 4:
            print(f"f({n}) = {result}")
        f0, f1, f2 = f1, f2, result
        n += 1
    return result

print("f(x) = a1*f(x-1) + a2*f(x-2) + a3*f(x-3) + p1*x + p2 + ex1*exp^x")
num_x = int(input("第x項 = "))
num_a1 = int(input("係數a1 = "))
num_a2 = int(input("係數a2 = "))
num_a3 = int(input("係數a3 = "))
num_p1 = int(input("係數p1 = "))
num_p2 = int(input("係數p2 = "))
num_ex1 = int(input("係數ex1 = "))
num_exp = int(input("指數底exp = "))
num_f0 = int(input("初始值f(0) = "))
num_f1 = int(input("初始值f(1) = "))
num_f2 = int(input("初始值f(2) = "))


"""
fn = fff(num_x, num_a1, num_a2, num_a3, num_p1, num_p2, num_ex1, num_exp, num_f0, num_f1, num_f2)
if num_x > 4:
    print(f"...\nf({num_x}) = {fn}")
else:
    print(f"f({num_x}) = {fn}")

#
def fff(x, a1,a2, ex1,exp, f0, f1):
    n = 2
    while n <= x:
        result = a1*f1 + a2*f0 + ex1*exp**n
        print(result)
        f0, f1 = f1, result
        n += 1
    return result

print("f(x) = a1*f(x-1) + a2*f(x-2) + ex1*exp^x")
num_x = int(input("第x項 = "))
num_a1 = int(input("係數a1 = "))
num_a2 = int(input("係數a2 = "))

num_ex1 = int(input("係數ex1 = "))
num_exp = int(input("指數底exp = "))

num_f0 = int(input("初始值f(0) = "))
num_f1 = int(input("初始值f(1) = "))


fn = fff(num_x, num_a1, num_a2, num_ex1, num_exp, num_f0, num_f1)
print(f"f({num_x}) = {fn}")
"""
