tickets = int(input('Количество билетов:'))
price = []
for i in range(1, tickets + 1):
    age = int(input(f"Возраст {i} клиента:"))
    if age < 18:
        price.append(0)
        print('До 18 лет - бесплатно')
    elif age <= 25:
        price.append(990)
        print('Стоимость 990 рублей')
    else:
        price.append(1390)
        print('Стоимость 1390 рублей')
print()
if tickets > 3:
    sale = (sum(price) - sum(price)*0.1)
    print('При покупке более 3 билетов скидка 10%.\nОбщая стоимость покупки с учетом скидки:', sale)
else:
    sale = (sum(price))
    print('Общая стоимость покупки составляет: ', sale) 