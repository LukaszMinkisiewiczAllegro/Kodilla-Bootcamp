import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def calculator():
    calc_type = input('Podaj dzialanie, poslugujac sie odpowiednia liczba: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie')
 
    a = input("Podaj skladnik 1")
    b = input("Podaj skladnik 2")

    if a.isnumeric() == False or b.isnumeric() == False:
        logging.WARNING("Musisz podac liczby")
    else:
        if calc_type == '2':
            logging.info("Odejmuje liczby, wynik to:")
            result = (int(a) - int(b))
        elif calc_type == '3':
            logging.info("Mnoze liczby, wynik to:")
            result = (int(a) * int(b))
        elif calc_type == '4':
            logging.info("Dziele liczby, wynik to:")
            result = (int(a) / int(b))
        else:
            logging.info("Dodaje liczby, wynik to:")
            result = (int(a) + int(b))   
    
    print(result)

if __name__ == "__main__":
    calculator()
        

