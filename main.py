from my_library import calculate_mean, factorial, is_prime
from my_library import reverse_string, count_vowels, capitalize_words

print("=" * 40)
print("ДЕМОНСТРАЦИЯ РАБОТЫ БИБЛИОТЕКИ")
print("=" * 40)

print("\nМатематические функции:")
print(f"  Среднее [1,2,3,4,5]: {calculate_mean([1,2,3,4,5])}")
print(f"  Факториал 5: {factorial(5)}")
print(f"  Число 17 простое? {is_prime(17)}")
print(f"  Число 25 простое? {is_prime(25)}")

print("\nСтроковые функции:")
print(f"  Переворот 'hello': {reverse_string('hello')}")
print(f"  Гласные в 'hello world': {count_vowels('hello world')}")
print(f"  Заглавные буквы: {capitalize_words('hello world from python')}")