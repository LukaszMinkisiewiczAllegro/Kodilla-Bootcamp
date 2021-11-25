zakupy = {'Piekarnia': ['Chleb', 'Bułki', 'Pączek'], 'Warzywniak': ['Marchew','Seler','Rukola']}

x = 0
for sklep, lista in zakupy.items():
    print(f'Idę do {sklep}, aby kupić: {lista}')
    x += len(lista)

print(f'W sumię kupię {x} przedmiotów')

divided_5 = []
divided_3 = []

for i in range(1,101):
    if i%5 == 0: divided_5.append(i)
    elif i%3 == 0: divided_3.append(i)

print(divided_3)
print(divided_5)