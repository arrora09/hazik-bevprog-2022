def szamol(a,b):
    print(a/b)

def check(a,b):
    try:
        szamol(a, b)
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    finally:
        print("Out of try except blocks")

if __name__=="__main__":
    while True:

        a=int(input("Enter 'a' value: "))
        b=int(input("Enter 'b' value: "))
        check(a,b)