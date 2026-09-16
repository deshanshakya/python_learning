try:
    print(1/0)
except:
    print("Executed if an exception occurs.")
#finally block is always executed no matter what, even though there is exception or not
finally:
    print("This is always executed.")