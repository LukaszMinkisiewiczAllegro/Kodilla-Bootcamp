import sys

def customized_hello(first_name, last_name, pronounce):
    print("Hello %s %s %s!" % (pronounce, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit(1)
    print(sys.argv)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    pronounce = sys.argv[3]
    customized_hello(first_name, last_name, pronounce)