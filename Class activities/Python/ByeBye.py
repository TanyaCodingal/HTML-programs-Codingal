valid=False

while not valid:
    try:
        n=int(input("Enter the num :"))
        while n%2==0:
            print("Bye!")
            n=int(input("Enter the num :"))
        valid=True

    except ValueError:
        print("ValueError - Handled :D")

    except ZeroDivisionError:
        print("ZeroDivisionError - Handled :D")

    except:
        print("GeneralError - Handled :D")

    finally:
        print("Tata!!")