# a = ['ram','shyam','hari','rita']

# print(a[1])
# del(a[3])
# print(a)

# print(a[0])

# a = [ ]
# b = list()

# a.insert(0,'Yunish')
# print(a)
# a.insert(1,"Shuvashis")
# print(a)
# a.insert(2,'Ritesh')
# print(a)
# a.pop(1)
# print(a)


# def find_length(s):
#     len(s)
#     l = len(s)
#     return l
# print(find_length("Ram"))

# def find_last_alphabet(s):
#     return s[-1]
# print(find_last_alphabet('Ram'))

# def find_reverse(s):
#     return s[::-1]
# print(find_reverse('ram'))

# def find_first_alphabet(s):
#     return s[0]
# print(find_first_alphabet('Ram'))

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(98))

# def is_even(n):
#     if n % 2 == 0:
#         print(f'{n} is even')
#     else:
#         print(f'{n} is odd')
# is_even(2)

# def is_divisible_by_5_and_10(n):
#     if n % 5 == 0 and n % 10 == 0:
#         print('Divisible')
#     else: 
#         print('Not divisible')
# is_divisible_by_5_and_10(100)

# def is_palindrome(s):
#     if s.lower() = s[::-1]lower()
#     return True
#     else:
#     return False
# is_palindrome('Ramar')


# def mean(*args):
#     return sum(args)/len(args)
# mean(1,2,3,4,5)

# def find_first_vowel(s):
#     for item in s:
#         if item.lower() in 'aeiou':
#             return item
# print(find_first_vowel('Yunish'))

def count_vowels(s):
    count = 0
    for item in s.lower():
        if item in 'aeiou':
            count = count + 1
    return count
print(count_vowels('Yunish'))

def count_consonants(s):
    count = 0
    for item in s.lower():
        if item in 'bcdfghjklmnpqrstvwxyz':
            count = count + 1
    return count
print(count_consonants('Yunish'))



















































































