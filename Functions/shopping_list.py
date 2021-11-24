def shopping(items, payment='card', shop='local shop'):
    result = ""
    result = result + "Ide na zakupy do %s.\n" % shop
    result = result + "Kupie nastepujace rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zaplacic, uzywam %s." % payment
    return result

if __name__ == "__main__":
    items_text = input("Podaj prosze produkty rozdzielone przecinkiem: ")
    items = items_text.split(',')
    shopping_result = shopping(items)
    print(shopping_result)