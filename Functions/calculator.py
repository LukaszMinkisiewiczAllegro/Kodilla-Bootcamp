import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def calculator():

    operator = '5'
    while operator not in ['1', '2', '3', '4']:
        operator = input('Podaj dzialanie, poslugujac sie odpowiednia liczba: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie')
 
    a = input("Podaj skladnik 1")
    b = input("Podaj skladnik 2")

    while True:
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print("Musisz podac liczby")
            a = input("Podaj skladnik 1")
            b = input("Podaj skladnik 2")
            continue
        else:
            break

        
    if operator == '1':
        num_to_add = [float(a),float(b)]
        more_num = input("Chcesz dodac wiecej niz 1 liczbe? Wpisz T lub N")

        while more_num.lower() == 't':
            c = input("Podaj kolejny skladnik")
            num_to_add.append(float(c))
            more_num = input("Chcesz dodac wiecej niz 1 liczbe? Wpisz T lub N")

        info = "Dodaje liczby, wynik to:"
        result = sum(num_to_add)

    elif operator == '2':
        info = "Odejmuje liczby, wynik to:"
        result = a - b
    
    elif operator == '3':
        info = "Mnoze liczby, wynik to:"
        result = a * b
    
    else:
        info = "Dziele liczby, wynik to:"
        result = a / b

    logging.info(info)
    print(result)

if __name__ == "__main__":
    calculator()
        

