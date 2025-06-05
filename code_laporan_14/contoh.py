# ✅ Soal Cerita 5: Permutasi Rekursif
# 💡 Soal:
# Buatlah program rekursif untuk menghitung permutasi.
# Rumus: P(n, r) = n! / (n-r)!.
# Contoh: P(10,4) ➜ Output: 5040.

def permutasi(m, n):
    if n == 0:
        return 1
    else:
        return permutasi(m, n-1) * (m-n+1)

print(permutasi(10, 4))  # Output: 5040

#🔴 Soal Cerita 3: Deret Fibonacci Rekursif
# 👧 Soal:
# Tini ingin mengetahui bilangan ke-n pada deret Fibonacci. Buat fungsi rekursif untuk membantu Tini.

# 📌 Contoh Kasus:
# Input: n=7 ➜ Deret: 1, 1, 2, 3, 5, 8, 13 ➜ Hasil: 13.

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(7))  # Output: 13


#  Soal Cerita 4: Konversi Basis Rekursif
# 👧 Soal:
# Iwan ingin tahu bagaimana mengubah bilangan desimal ke basis lain (2, 8, atau 16) dengan fungsi rekursif. Bantu Iwan membuat fungsinya!

# 📌 Contoh Kasus:
# Input: angka=9, basis=8 ➜ Hasil: 11.
def toBasis(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toBasis(n//base, base) + convertString[n%base]

print(toBasis(9, 8))  # Output: 11
