import random
from math import gcd

def coprime(a, b):
    return gcd(a, b) == 1


def prime_number():
    n = 1024  # количество чисел
    arr = []
    for i in range(n + 1):  # заполнение массива числами от 0 до n
        arr.append(i)
    arr[1] = 0  # генерация простых чисел
    i = 2
    while i ** 2 <= n:
        if arr[i] != 0:
            j = i ** 2
            while j <= n:
                arr[j] = 0
                j += i
        i += 1

    arr = set(arr)  # преобразование массива в set (set удаляет все повторяющеся элементы)
    arr.remove(0)  # удаление значения 0 из сета
    arr = list(arr)
    arr.sort()
    index = random.randint(0, len(arr)-1)
    num1 = arr[index]
    index = random.randint(0, len(arr) - 1)
    num2 = arr[index]
    print(arr)
    return arr, num1, num2

# RSA
arr1, p, q = prime_number()
arr1 = list(arr1)
print("p =", p)
print("q =", q)
modul = p * q
print("modul =", modul)
Eiler_func = (p - 1) * (q - 1)
print("Eiler_func =", Eiler_func)

public_exponent = random.choice(arr1)
print("public_exponent =", public_exponent)


while True:
    if not(1 < public_exponent < Eiler_func) or not coprime(public_exponent, Eiler_func) :
        print("change public_exponent")
        arr1.remove(public_exponent)
        public_exponent = random.choice(arr1)
        print("public_exponent_new =", public_exponent)
    else:
        break

for private_exponent in range(3, Eiler_func, 2):
        if private_exponent * public_exponent % Eiler_func == 1:
            break
print("private_exponent =", private_exponent)

m = int(input("Enter number: "))

c = (m ** public_exponent) % modul
print("encrypted =", c)

m_1 = (c ** private_exponent) % modul

print("decrypted =", m_1)

if m_1 == m:
    print("\t\t Success!")
else:
    print("Fail!")