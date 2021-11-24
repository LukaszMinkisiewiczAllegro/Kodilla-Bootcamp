def say_hello(name):
    result = "Hello {}".format(name)
    return result

if __name__ == "__main__":
    input_name = input("Give me your name")
    welcome = say_hello(input_name)

    print(f"The program was called with this parameter - {input_name}")
    print(f"The parameter's type was - {type(input_name)}")

    print(welcome)