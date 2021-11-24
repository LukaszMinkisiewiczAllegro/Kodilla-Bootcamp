import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def add(a,b):
    print(a+b)


if __name__ == "__main__":
     logging.debug(f"Parameters: {sys.argv}")
     logging.debug(f"Types: {type(sys.argv[1])}, {type(sys.argv[2])}")

     a = int(sys.argv[1])
     b = int(sys.argv[2])
     add(a, b)
