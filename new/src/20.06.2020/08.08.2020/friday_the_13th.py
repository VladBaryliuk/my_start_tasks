import datetime
# day = 1
# month = 1
# year = int(input("enter year"))
# date = datetime.date(year,month,day)
# for i in range(365):
#     date = datetime.date(year,month,day)
#     if day == 13 and
#         print("found Friday the 13th", date)
#     else:
#         day +=1
#     if day == 31:
#         month += 1
#     if month == 12:
#         break
year = int(input('Введите год: '))
fridays = 0
for month in range(1, 13):
    if datetime.date(year, month, 13).weekday() == 4:
        fridays += 1
        print(f'Пятница 13-того найдена: {datetime.date(year, month, 13)}')
print(f"В {year} году обнаружено {fridays} пятниц 13-того")