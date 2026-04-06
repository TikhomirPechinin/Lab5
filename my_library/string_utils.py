def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("Входное значение должно быть строкой")
    return s[::-1]

def count_vowels(s):
    if not isinstance(s, str):
        raise TypeError("Входное значение должно быть строкой")
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)

def capitalize_words(s):
    if not isinstance(s, str):
        raise TypeError("Входное значение должно быть строкой")
    return ' '.join(word.capitalize() for word in s.split())