try:
    print(1/0)
except:
    print("Executed if an exception occurs.")
finally:
    print("This is always executed.")