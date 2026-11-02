def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
        return count
print("Number of vowels =", count_vowels("Hello World"))