# bug/error

#Syntax error
# occurs because of typo 
# if you write code that python complex doesnot under stand syntax error occurs
#Syntax error is the most easiest error to fix

#Logical error
# This is the most difficult error to fix.
# age = int(input('Enter age: '))
# if age >= 18:
#     print('You can vote')
# else:
#     print('You cannot vote')

# Runtime error
# Program terminates unexpectedly
# while True:
#     fn = int(input('Enter first number: '))
#     ln = int(input('Enter second number: '))
#     print(fn/ln)

# try:
#     # Risky code
#     # Code that can throw errors
# except:
#     # alternative code
#     # Code to run when there are no errors

# while True:
#     try:
#         fn = int(input('Enter first number: '))
#         ln = int(input('Enter a second number: '))
#         print(fn/ln)
#     except:
#         print('An error occured')

# while True:
#     try:
#         fn = int(input('Enter first number: '))
#         ln = int(input('Enter a second number: '))
#         print(fn/ln)
#     except Exception as e:
#         print(type(e))

while True:
    try:
        fn = int(input('Enter first number: '))
        ln = int(input('Enter a second number: '))
        print(fn/ln)
    except ZeroDivisionError:
        print('Second number cannot be zero')
    except ValueError:
        print('Inputs must be numbers')
    except:
        print('An error occured')




