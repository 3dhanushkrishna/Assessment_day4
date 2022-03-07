def word(a):
    return a == a[::-1]
x = input("enter the word: ")
str = word(x)
print(str)
if str:
    print("it is palindrome")
else:
    print("it is not a palindrome")
