def prostota(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        else:
            pass
    return True
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def triangle(a, b, c):
    if ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
        print ("Нема ніякого трикутника")
    else:
        if (a**2<b**2+c**2 or b**2<a**2+c**2 or c**2<b**2+a**2):
            print ("Трикутник тупокутний")
        else:
            print ("Трикутник є, але НЕ тупокутний")
def pyatirka(n):
    if n%5!=0:
        return False
    while n%5==0:
        n=n/5
    if n%5!=0 and n!=1:
        return False
    else:
        return True
        
def NSD(a, b):
    try:
        if b > a:
        a, b = b, a
        while b > 0:
            a, b = b, (a % b)
        return a
    except:
        return "MONKEY"
    
    
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print()