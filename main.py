def greet(name):
    print("Hello, " + name + ". Good morning!")
greet('Penguin')

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num
print("Absolute value of 89", absolute_value(89))
print("Absolute value of -189", absolute_value(-189))


def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) -1

    while right_pos>=left_pos:
     if not string[left_pos] == [right_pos]:
        return False
     left_pos += 1
     right_pos = 1
    return True
print("Is this a palindrome?")
print(isPalindrome('Malayalam'))