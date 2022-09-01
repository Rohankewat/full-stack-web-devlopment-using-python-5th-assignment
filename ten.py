n = int(input("Enter three digit number "))  # Question no:- 6
sum = 0
while n != 0:
    if n == 100:
        print("middle digit of three digit number is 0")
        break
    elif n != 100:
        r = n%10
        sum = sum * 10 + 1
        if 10 <= sum <= 99:
            print("middle digit of three digit number is",r)
            break
        n = n//10
print()

