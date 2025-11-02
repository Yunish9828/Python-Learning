# Q. Write a function that takes string and checks wether vowel is present in the string or not
# Q. Write a function that takes string and checks wether consonant is present in the string or not
# Q. Write a function that takes string and returns the total number of vowels present in the string
# Q. Write a function that takes string and returns the total number of consonants present in the string
# Q. Write a function that takes string and check wether the string is palindrome or not disregarding the case sensitivity


# Q. Write a function that takes string and checks wether vowel is present in the string or not
# def is_vowel(a):
#     vowel = 'aeiou'
#     if a.lower() in vowel:
#         return True
#     else:
#         return False
# print(is_vowel('e'))


# Q. Write a function that takes string and checks wether consonant is present in the string or not
# def is_consonant(b):
#     consonant = 'bcdfghjklmnpqrstvwxyz'
#     if b.lower() in consonant:
#         return True
#     else:
#         return False
# print(is_consonant('z'))

# Q. Write a function that takes string and returns the total number of vowels present in the string
# def number_vowel(v):
#     vowel = 'aeiou'
#     a = 0


# Q. Write a function that takes string and returns the total number of consonants present in the string
# def number_consonant(c):
#     consonant = 'bcdfghjklmnpqrstvwxyz'


# # Q. Write a function that takes string and check wether the string is palindrome or not disregarding the case sensitivity
def palindrome(p):
    p = p.lower()
    pal = input("Enter a string to check for palindrome: ")
    if p == pal[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
input(palindrome)

        



    








