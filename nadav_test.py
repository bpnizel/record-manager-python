def main():
    foo()

def foo():
    bar()

def bar():
    raise ZeroDivisionError("Hello")


try:
    main()
except ZeroDivisionError as e:
    print("Hey, i cought it")
    print(e)