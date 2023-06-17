def gcd(m, n): #最大公因數
    return m if n == 0 else gcd(n, m % n)

def lcm(m, n): #最小公倍數
    return m * n // gcd(m, n)
    
m = int(input("輸入 m："))
n = int(input("輸入 n："))
print("Gcd: ", gcd(m, n))
print("Lcm: ", lcm(m, n))