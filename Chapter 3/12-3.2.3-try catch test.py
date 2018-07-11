s= input("Enter a number: ")
try:
    number = float(s)
    answer = number * number
    print(number, " * ", number, " = ", answer)
except:
    print("It's not a number!")