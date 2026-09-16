try:
    result = 5/0
    print(result)
    
    my_list = [1, 2, 3]
    print(my_list[20])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index is wrong.")