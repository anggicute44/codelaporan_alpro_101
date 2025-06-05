#  Latihan 13.1: Cek Bilangan Prima (Rekursif)
# 💡 Tujuan:
# Cek apakah bilangan n adalah prima atau bukan.

def is_prime(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor+1)

# Contoh penggunaan
print(is_prime(7))  # Output: True
print(is_prime(10)) # Output: False


# Latihan 13.2: Palindrom Rekursif
# 💡 Tujuan:
# Cek apakah sebuah string adalah palindrom.

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Hilangkan spasi dan jadikan huruf kecil
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Contoh penggunaan
print(is_palindrome("radar"))       # Output: True
print(is_palindrome("hello"))       # Output: False
print(is_palindrome("A man a plan a canal Panama"))  # Output: True


# Latihan 13.3: Jumlah Deret Ganjil dari 1 + 3 + 5 + ... + n
# 💡 Tujuan:
# Hitung jumlah deret ganjil dari 1 hingga n (n ganjil).

# ✅ Jawaban:

def jumlah_deret_ganjil(n):
    if n == 1:
        return 1
    else:
        return n + jumlah_deret_ganjil(n-2)

# Contoh penggunaan
print(jumlah_deret_ganjil(7))  # Output: 16 (1+3+5+7=16)

# ✅ Latihan 13.4: Hitung Jumlah Digit Bilangan
# 💡 Tujuan:
# Hitung jumlah digit suatu bilangan.

def jumlah_digit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + jumlah_digit(n // 10)

# Contoh penggunaan
print(jumlah_digit(234))  # Output: 9 (2+3+4)


# Latihan 13.5: Hitung Kombinasi (C(n, r)) Rekursif
# 💡 Rumus Kombinasi:

# ✅ Jawaban (dengan fungsi faktorial rekursif):

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

def kombinasi(n, r):
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# Contoh penggunaan
print(kombinasi(5, 2))  # Output: 10
print(kombinasi(10, 4)) # Output: 210

# Contoh Soal Cerita 1: Menjumlahkan Deret Bilangan
# 👧 Soal:
# Dina ingin menghitung jumlah semua bilangan dari 1 sampai n. Buatkan fungsi rekursif untuk membantu Dina.

# 📌 Contoh Kasus:
# Input: n=5 ➜ 1+2+3+4+5=15

def jumlah_deret(n):
    if n == 1:
        return 1
    else:
        return n + jumlah_deret(n-1)

print(jumlah_deret(5))  # Output: 15


#  Contoh Soal Cerita 2: Membalikkan String
# 👧 Soal:
# Rudi ingin membalikkan kata yang dia masukkan secara rekursif. Bantu Rudi membuat programnya!

# 📌 Contoh Kasus:
# Input: "kucing" ➜ Output: "gnicuk"

# ✅ Jawaban:
def balik_string(s):
    if len(s) == 0:
        return s
    else:
        return balik_string(s[1:]) + s[0]

print(balik_string("kucing"))  # Output: gnicuk

#  Contoh Soal Cerita 4: Jumlah Elemen List
# 👧 Soal:
# Lina memiliki daftar angka dan ingin menjumlahkan semua elemennya secara rekursif. Bantu Lina!

# 📌 Contoh Kasus:
# Input: [1, 2, 3, 4] ➜ 10

def jumlah_list(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + jumlah_list(l[1:])

print(jumlah_list([1, 2, 3, 4]))  # Output: 10
