# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

#Решение через list
# month = int(input('Введите число месяца в году:'));
# seasons = ['Зима', 'Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима'];
# print(seasons[month]);
#Решение через dict
seasonsMonths = {'Зима' : (12, 1, 2), 'Весна' : (3, 4, 5),'Лето' : (6, 7, 8), 'Осень' : (9, 10, 11)};
month = int(input('Введите число месяца в году: '));
for key in seasonsMonths.keys():
    if month in seasonsMonths[key]:
        print(key);