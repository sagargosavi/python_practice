#123  > 321

def reverse(n):
    rev = 0;
    negative = n < 0
    num = abs(n)
    while num != 0:
        rev = rev*10+num%10
        num = num//10
    return rev if not negative else -(rev)

