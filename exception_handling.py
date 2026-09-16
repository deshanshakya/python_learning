# try block is run if there is no any issues here
try:
    numerator = int(input("Enter a numerator"))
    denominator = int(input("Enter a denominator"))
    result = numerator/denominator
    print(result)

    my_list = [1,2,3]
    index = int(input("enter index"))
    print(my_list[index])
# if ZeroDivisorError exception occurs then
except ZeroDivisionError:
    print("Divisor cannot be 0")
except IndexError:
    print("Index error")