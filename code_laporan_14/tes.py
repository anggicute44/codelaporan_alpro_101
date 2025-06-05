def faktorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * faktorial(n-1)
def perkalian(a, b):
    if b == 1:
        return a
    else:
        return a + perkalian(a, b-1)
def pangkat(a, b):
    if b == 1:
        return a
    else:
        return a * pangkat(a, b-1)
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
def toBasis(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toBasis(n//base, base) + convertString[n%base]
def permutasi(m, n):
    if n == 0:
        return 1
    else:
        return permutasi(m, n-1) * (m-n+1)
    
 #Hitung Jumlah Angka 0 di Bilangan   
def hitung_nol(n):
    if n == 0:
        return 1
    elif n < 10:
        return 0
    else:
        if n % 10 == 0:
            return 1 + hitung_nol(n // 10)
        else:
            return hitung_nol(n // 10)

print(hitung_nol(102030))  # Output: 3
